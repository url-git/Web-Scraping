#!/usr/bin/env python3
"""
Web Scraper - pobiera tweety z X (Twitter) używając Apify API.
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

try:
    from apify_client import ApifyClient
except ImportError:
    print("Installing apify-client...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "apify-client"])
    from apify_client import ApifyClient

try:
    from dotenv import load_dotenv
except ImportError:
    print("Installing python-dotenv...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv"])
    from dotenv import load_dotenv

load_dotenv()

ACTOR_ID = "kaitoeasyapi/twitter-x-data-tweet-scraper-pay-per-result-cheapest"
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def get_api_token():
    """Pobiera API token z zmiennej środowiskowej lub pliku .env"""
    token = os.getenv("APIFY_API_TOKEN")
    if token:
        return token

    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        token = os.getenv("APIFY_API_TOKEN")
        if token:
            return token

    print("❌ Brak API token!")
    print("   1. Wejdź na https://console.apify.com/settings")
    print("   2. Skopiuj token z sekcji 'API tokens'")
    print("   3. Wklej do pliku .env jako APIFY_API_TOKEN=...")
    sys.exit(1)


def scrape_tweets(query, max_items=20, query_type="Top"):
    """Pobiera tweety dla danego zapytania"""
    client = ApifyClient(token=get_api_token())

    input_data = {
        "twitterContent": query,
        "maxItems": max_items,
        "queryType": query_type,
        "lang": "en",
        "include:nativeretweets": True
    }

    print(f"🔍 Szukam: '{query}' ({max_items} tweetów, {query_type})...")

    try:
        run = client.actor(ACTOR_ID).call(run_input=input_data)

        if not run or not run.get("defaultDatasetId"):
            print(f"⚠️  Brak wyników dla: {query}")
            return []

        items = list(client.dataset(run.get("defaultDatasetId")).iterate_items())

        if not items:
            print(f"⚠️  Brak wyników w datasecie dla: {query}")
            return []

        print(f"✅ Pobrano {len(items)} tweetów dla: {query}")
        return items

    except Exception as e:
        print(f"❌ Błąd podczas pobierania '{query}': {e}")
        return []


def filter_tweets(items, keyword):
    """Filtruje tweety zawierające keyword"""
    filtered = []
    keyword_lower = keyword.lower()

    for item in items:
        text = item.get("text", "")
        if keyword_lower in text.lower():
            filtered.append(item)

    print(f"📝 Przefiltrowano: {len(filtered)}/{len(items)} tweetów zawiera '{keyword}'")
    return filtered


def format_to_markdown(items, keyword):
    """Konwertuje tweety do formatu Markdown"""
    if not items:
        return f"## {keyword}\n\nBrak tweetów do wyświetlenia.\n"

    md = f"## {keyword}\n\n"
    md += f"*Pobrano: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"

    for item in items:
        author = item.get("author", {})
        username = author.get("userName", "unknown")
        name = author.get("name", username)
        text = item.get("text", "")
        created_at = item.get("createdAt", "")
        like_count = item.get("likeCount", 0)
        retweet_count = item.get("retweetCount", 0)
        view_count = item.get("viewCount", 0)
        url = item.get("url", "")

        md += f"### @{username}\n"
        md += f"**{name}** | "
        md += f"Data: {created_at} | "
        md += f"❤️ Polubienia: {like_count} | "
        md += f"🔁 {retweet_count} | "
        md += f"👁 {view_count}\n\n"
        md += f"{text}\n\n"
        if url:
            md += f"[Link do tweeta]({url})\n"
        md += "\n---\n\n"

    return md


def save_to_file(content, filename):
    """Zapisuje treść do pliku"""
    filepath = OUTPUT_DIR / filename
    filepath.write_text(content, encoding="utf-8")
    print(f"💾 Zapisano: {filepath}")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Pobieranie tweetów z X")
    parser.add_argument("-q", "--query", nargs="+", default=["OpenCode"],
                      help="Hasła wyszukiwania (można podać kilka oddzielonych spacją)")
    parser.add_argument("-m", "--max", type=int, default=5, help="Maksymalna liczba tweetów na frazę")
    parser.add_argument("-t", "--type", default="Top", choices=["Top", "Latest"],
                      help="Typ wyszukiwania")

    args = parser.parse_args()

    keywords = args.query

    all_markdown = "# Web Scraping - X Tweets\n\n"
    all_markdown += f"*Data pobrania: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"

    for keyword in keywords:
        items = scrape_tweets(keyword, args.max, args.type)
        filtered = filter_tweets(items, keyword)
        markdown = format_to_markdown(filtered, keyword)
        all_markdown += markdown

    filename = f"tweets-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.md"
    save_to_file(all_markdown, filename)

    print(f"\n✅ Gotowe! Wynik w: {OUTPUT_DIR / filename}")


if __name__ == "__main__":
    main()
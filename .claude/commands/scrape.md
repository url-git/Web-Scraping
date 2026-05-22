# scrape

Scrapuje tweety z X (Twitter) używając Apify API i generuje raport po polsku.

> [!IMPORTANT]
> **WSZYSTKIE RAPORTY MUSZĄ BYĆ W JĘZYKU POLSKIM.**
> Sekcja "Co to znaczy" musi zawierać 5-6 merytorycznych zdań.

## Krok 1: Sprawdź datę i konfigurację

```bash
date +%Y-%m-%d
cat /Users/p/Documents/dev/Web-Scraping/.env
```

## Krok 2: Uruchom scraping (TYLKO RAZ, wszystkie frazy naraz)

```bash
cd /Users/p/Documents/dev/Web-Scraping && source venv/bin/activate && python scrape.py -q "OpenCode" "Cloud Code" "OpenRouter" "OpenAI Codex" "Antigravity" "@warpdotdev" "Gemini CLI" "@stape_io" "n8n" -m 10 -t Top -l 100
```

## Krok 3: Wygeneruj raport po polsku

Przeczytaj `output/raw-tweets-{YYYY-MM-DD}.md` i utwórz `output/tweets-{YYYY-MM-DD}.md`.

### Format pliku wynikowego

```markdown
# Web Scraping - X Tweets

*Data pobrania: YYYY-MM-DD HH:MM*

## Podsumowanie

[3-4 zdania ogólnego podsumowania trendów — po polsku.]

---

## [Słowo kluczowe]

*Pobrano: YYYY-MM-DD HH:MM*

### @użytkownik
**Nazwa** | Data: [Data oryg.] | ❤️ Polubienia: [Liczba] | 🔁 [Retweety] | 👁 [Wyświetlenia]

[Treść tweeta przetłumaczona w całości na polski]

> **Co to znaczy:** [5-6 PEŁNYCH ZDAŃ wyjaśniających praktyczne znaczenie dla programisty. Co ta informacja oznacza i jak wykorzystać te narzędzia w codziennej pracy. Unikaj ogólników.]

---
```

### Zasady

- Tweety ewidentnie spoza IT (UFO, ezoteryka) — pomijaj nawet jeśli przeszły przez filtr skryptu
- Nazwy własne i daty systemowe mogą zostać po angielsku — reszta po polsku
- Jeden plik końcowy, nie twórz wielu raportów

## Krok 4: Git commit i push

```bash
cd /Users/p/Documents/dev/Web-Scraping && git add -A && git commit -m "Scrape tweets for $(date +%Y-%m-%d): [krótki opis trendów]" && git push
```

Po zapisaniu pliku wyświetl użytkownikowi podsumowanie w czacie.

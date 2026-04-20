# Web Scraping

Projekt do scrapowania danych z X (Twitter) używając Apify API.

## Wymagania

### 1. Utwórz środowisko wirtualne

```bash
# macOS / Linux:
python -m venv venv

# Windows:
python -m venv venv
```

### 2. Aktywuj środowisko wirtualne

```bash
# macOS / Linux:
source venv/bin/activate

# Windows (PowerShell):
venv\Scripts\Activate

# Windows (CMD):
venv\Scripts\activate.bat
```

### 3. Zainstaluj zależności

```bash
pip install -r requirements.txt
```

> **Uwaga:** Zawsze aktywuj venv przed uruchomieniem projektu (`source venv/bin/activate`). Środowisko wirtualne izoluje zależności tego projektu od innych.

## Konfiguracja

1. Skopiuj plik konfiguracyjny:
```bash
cp config.example.env .env
```

2. Dodaj swój API token z https://console.apify.com/settings

## Użycie

```bash
python scrape.py -q "OpenCode" "Cloud Code" -m 5 -t Top
```

### Parametry:
- `-q` --query: hasło wyszukiwania (domyślnie: OpenCode)
- `-m` --max: liczba tweetów na frazę (domyślnie: 5)
- `-t` --type: Top lub Latest (domyślnie: Top)

## Wyniki

Wyniki zapisują się w folderze `output/`:
```
output/tweets-2026-04-18.md
```

## Uruchomienie z Open Code

Gdy potrzebujesz pobrać tweety, powiedz:
- "Pobierz tweety o OpenCode z X"
- lub "/scraper"

Skrypt automatycznie pobiera tweety dla OpenCode i CloudCode i zapisuje w `output/`.
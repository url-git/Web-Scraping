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
# Najpierw aktywuj środowisko:
source venv/bin/activate

# Uruchom skrypt:
python scrape.py -q "OpenCode" "Cloud Code" -m 5 -t Top
```

### Parametry:
- `-q` --query: hasło wyszukiwania (domyślnie: OpenCode)
- `-m` --max: liczba tweetów na frazę (domyślnie: 5)
- `-t` --type: Top lub Latest (domyślnie: Top)
- `-l` --likes: minimalna liczba polubień (domyślnie: 20)

## Wyniki

Wyniki zapisują się w folderze `output/`:
- `output/raw-tweets-{YYYY-MM-DD}.md`: Surowe dane (angielski/oryginalny).
- `output/tweets-{YYYY-MM-DD}.md`: **Ostateczny raport** (przetłumaczony na polski, z komentarzami).

## Uruchomienie z Open Code

### Wersja 1: Domyślne frazy (OpenCode + Cloud Code)

Polecenie dla agenta:
```
Korzystając ze Skilla z '/Users/p/Documents/dev/Web-Scraping/.opencode/skills/scraper/SKILL.md', pobierz nowe tweety z serwisu X. Wynikowy plik markdown zapisz w '/Users/p/Documents/dev/Web-Scraping/output/'.
```

Komenda bash (do uruchomienia ręcznego):
```bash
cd /Users/p/Documents/dev/Web-Scraping && source venv/bin/activate && python scrape.py -q "OpenCode" "Cloud Code" -m 10 -t Top -l 100
```

### Wersja 2: Własne frazy

Polecenie dla agenta:
```
Korzystając ze Skilla z '/Users/p/Documents/dev/Web-Scraping/.opencode/skills/scraper/SKILL.md', pobierz nowe tweety z serwisu X dla fraz [OpenCode, Cloud Code, OpenRouter, OpenAI Codex, Antigravity, @warpdotdev, Gemini CLI, @stape_io]. Wynikowy plik markdown zapisz w '/Users/p/Documents/dev/Web-Scraping/output/'.
```

Komenda bash (do uruchomienia ręcznego):
```bash
cd /Users/p/Documents/dev/Web-Scraping && source venv/bin/activate && python scrape.py -q "OpenCode" "Cloud Code" "OpenRouter" "OpenAI Codex" "Antigravity" "@warpdotdev" "Gemini CLI" "@stape_io" -m 10 -t Top -l 100
```

### Co robi agent:
1. Ładuje skill z podanej ścieżki
2. Sprawdza plik .env i API token
3. Uruchamia skrypt scrape.py z podanymi parametrami
4. Pobiera surowe tweety do `output/raw-tweets-{YYYY-MM-DD}.md`
5. Tłumaczy i formatuje do pliku `output/tweets-{YYYY-MM-DD}.md` z komentarzami w języku polskim

### Ścieżki:
- **Skill:** `/Users/p/Documents/dev/Web-Scraping/.opencode/skills/scraper/SKILL.md`
- **Output:** `/Users/p/Documents/dev/Web-Scraping/output/tweets-{YYYY-MM-DD}.md`
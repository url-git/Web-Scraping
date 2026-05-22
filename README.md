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

> **Filtrowanie wykluczające:** Skrypt automatycznie odrzuca tweety zawierające frazy z listy `EXCLUDE_WORDS` (np. UFO, alien). Aby dodać nowe, edytuj stałą w `scrape.py:36`.

## Wyniki

Wyniki zapisują się w folderze `output/`:
- `output/raw-tweets-{YYYY-MM-DD}.md`: Surowe dane (angielski/oryginalny).
- `output/tweets-{YYYY-MM-DD}.md`: **Ostateczny raport** (przetłumaczony na polski, z komentarzami).

## Automatyczna rutyna (Claude Code Routines)

Projekt ma skonfigurowaną rutynę w chmurze Anthropic — scrapowanie odpala się automatycznie bez udziału użytkownika i bez konieczności włączonego MacBooka.

| Pole | Wartość |
|------|---------|
| **Nazwa** | Twitter Scraper — Pn/Śr/Pt |
| **Harmonogram** | Poniedziałek, Środa, Piątek o 03:00 Warsaw (01:00 UTC) |
| **Model** | claude-sonnet-4-6 |
| **Repozytorium** | github.com/url-git/Web-Scraping |
| **Frazy** | OpenCode, Cloud Code, OpenRouter, OpenAI Codex, Antigravity, @warpdotdev, Gemini CLI, @stape_io, n8n |
| **Token Apify** | zapisany w konfiguracji rutyny na serwerach Anthropic |
| **Zarządzanie** | https://claude.ai/code/routines |

### Jak działa pipeline:

1. Cron na serwerach Anthropic odpala agenta o ustalonej godzinie
2. Agent klonuje repo z GitHub (tymczasowa kopia robocza)
3. Tworzy plik `.env` z tokenem Apify (token jest w prompcie rutyny)
4. Uruchamia `scrape.py` ze wszystkimi 9 frazami jednocześnie
5. Generuje raport po polsku (`output/tweets-YYYY-MM-DD.md`)
6. Commituje i pushuje wyniki na GitHub
7. Kopia robocza jest usuwana po zakończeniu sesji

### Co jest gdzie przechowywane:

| Zasób | Lokalizacja |
|-------|-------------|
| Kod projektu (`scrape.py`, `output/`) | GitHub |
| Konfiguracja rutyny i prompt | Serwery Anthropic |
| Token Apify | Serwery Anthropic (w prompcie rutyny) |
| Plik `.env` | Lokalnie (gitignored) — tworzony przez agenta na czas sesji |

---

## Ręczne uruchomienie

### Z Claude Code (polecenie `/scrape`)

Wpisz `/scrape` w Claude Code — polecenie jest zdefiniowane w `.claude/commands/scrape.md` i zawiera pełny workflow: scraping → raport po polsku → git push.

### Z OpenCode (skill)

Polecenie dla agenta:
```
Korzystając ze Skilla z '/Users/p/Documents/dev/Web-Scraping/.opencode/skills/scraper/SKILL.md', pobierz nowe tweety z serwisu X dla fraz [OpenCode, Cloud Code, OpenRouter, OpenAI Codex, Antigravity, @warpdotdev, Gemini CLI, @stape_io, n8n]. Wynikowy plik markdown zapisz w '/Users/p/Documents/dev/Web-Scraping/output/'. Po zapisaniu plików, dodaj nowe pliki Markdown do repozytorium git, zrób commit i push do GitHuba.
```

### Z terminala (bash)

```bash
cd /Users/p/Documents/dev/Web-Scraping && source venv/bin/activate && python scrape.py -q "OpenCode" "Cloud Code" "OpenRouter" "OpenAI Codex" "Antigravity" "@warpdotdev" "Gemini CLI" "@stape_io" "n8n" -m 10 -t Top -l 100
```

### Parametry `scrape.py`:

| Flaga | Opis | Domyślnie |
|-------|------|-----------|
| `-q` | Frazy wyszukiwania (wiele naraz, oddzielone spacją) | OpenCode |
| `-m` | Maksymalna liczba tweetów na frazę | 5 |
| `-t` | Typ wyników: `Top` lub `Latest` | Top |
| `-l` | Minimalna liczba polubień | 20 |

> **Ważne:** Zawsze podawaj wszystkie frazy w jednym wywołaniu `-q`. Uruchamianie skryptu osobno dla każdej frazy tworzy duplikaty pliku wyjściowego.

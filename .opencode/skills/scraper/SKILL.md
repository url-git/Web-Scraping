# scraper

> [!IMPORTANT]
> **WSZYSTKIE RAPORTY MUSZĄ BYĆ W JĘZYKU POLSKIM.** 
> Plik wynikowy Markdown musi być w pełni przetłumaczony i sformatowany według poniższego wzorca. Sekcja "Co to znaczy" musi zawierać 5-6 merytorycznych zdań.

Scrapuje tweety z X (Twitter) używając Apify API i zapisuje wyniki do Markdown.

## Uruchomienie

Gdy użytkownik poprosi o pobranie tweetów z X, wykonaj następujące kroki:

### Krok 1: Sprawdź konfigurację

Sprawdź czy istnieje plik `.env` w projekcie `/Users/p/Documents/dev/Web-Scraping/`:
```
cat /Users/p/Documents/dev/Web-Scraping/.env
```
Jeśli plik nie istnieje lub nie zawiera `APIFY_API_TOKEN` - poproś użytkownika o token.

### Krok 2: Uruchom skrypt (TYLKO RAZ)

Jeśli użytkownik nie podał konkretnej frazy - użyj domyślnych: "OpenCode" i "Cloud Code".

Uruchom skrypt podając wszystkie słowa kluczowe jednocześnie, aby uniknąć tworzenia wielu plików:
```
cd /Users/p/Documents/dev/Web-Scraping && source venv/bin/activate && python scrape.py -q "OpenCode" "Cloud Code" -m 10 -t Top -l 100
```

Jeśli użytkownik podał własną frazę (np. "AI" "machine learning"):
```
cd /Users/p/Documents/dev/Web-Scraping && source venv/bin/activate && python scrape.py -q "AI" "machine learning" -m 10 -t Top -l 100
```

### Krok 3: Wygeneruj raport w języku polskim

Skrypt wygeneruje plik surowy: `output/raw-tweets-{YYYY-MM-DD}.md`. 
Twoim zadaniem jest przeczytać ten plik, a następnie **utworzyć nowy plik** `output/tweets-{YYYY-MM-DD}.md` z pełnym tłumaczeniem i formatowaniem premium.

#### Wymagany format pliku `tweets-{YYYY-MM-DD}.md`:

```markdown
# Web Scraping - X Tweets

*Data pobrania: YYYY-MM-DD HH:MM*

## Podsumowanie

[Tutaj napisz w 3-4 zdaniach ogólne podsumowanie tego, co ciekawego dzieje się w trendach dla tych haseł - po polsku.]

---

## [Słowo kluczowe 1]

*Pobrano: YYYY-MM-DD HH:MM*

### @użytkownik
**Nazwa** | Data: [Data oryg.] | ❤️ Polubienia: [Liczba] | 🔁 [Retweety] | 👁 [Wyświetlenia]

[Treść tweeta przetłumaczona w całości na język polski]

> **Co to znaczy:** [Tutaj napisz 5-6 ZDAŃ wyjaśniających praktyczne znaczenie tego wpisu. Co ta informacja oznacza dla programisty i jak wykorzystać te narzędzia w codziennej pracy z OpenCode lub CloudCode. Unikaj ogólników.]

---
```

## Uwagi

- **Automatyczna deduplikacja**: Skrypt automatycznie pomija duplikaty.
- **Język**: Cały plik `tweets-*.md` (poza nazwami własnymi i datami systemowymi) musi być po polsku.
- **Długość komentarza**: Bezwzględnie pilnuj, aby "Co to znaczy" miało 5-6 pełnych zdań.
- **Jeden plik końcowy**: Nie twórz wielu plików raportów. Wynik końcowy to jeden plik `tweets-{YYYY-MM-DD}.md`.
- **Prezentacja**: Po zapisaniu pliku, wyświetl użytkownikowi podsumowanie w czacie.
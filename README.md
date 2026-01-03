# DNA Sequence Fetcher

## Opis projektu

Ten projekt pokazuje, jak pobierać dane biologiczne w formacie FASTA z publicznej bazy GenBank (NCBI) przy użyciu Pythona i biblioteki **Biopython**.  

Celem projektu jest:

- pobranie sekwencji DNA po podanych identyfikatorach,
- filtrowanie sekwencji według długości (do 200 nukleotydów),
- zapis wyników do pliku w formacie FASTA.

Projekt jest przykładem **pracy z zewnętrznymi źródłami danych, przetwarzania danych i zapisu wyników** w Pythonie.

---

## Technologie i biblioteki

- **Python 3**
- **Biopython** – do pobierania i parsowania sekwencji biologicznych
- Standardowe moduły Pythona: `os`, `datetime` (jeśli potrzebne do zapisu plików i daty)

---

## Jak działa kod

1. Ustawienie adresu e-mail użytkownika – wymagane przez NCBI do pobierania danych.
2. Zdefiniowanie listy identyfikatorów sekwencji DNA (`ids`) z GenBanku.
3. Pobranie sekwencji w formacie FASTA przy użyciu funkcji `Entrez.efetch`.
4. Wczytanie sekwencji do programu za pomocą `SeqIO.parse`.
5. Filtrowanie sekwencji, aby uwzględnić tylko te o długości do 200 nukleotydów.
6. Zamknięcie połączenia z bazą danych.
7. Wyświetlenie liczby pobranych sekwencji spełniających kryterium długości.
8. Zapisanie wyników do pliku `sekwencje_do_200nt.txt` w formacie FASTA.

---

## Przykładowe zastosowania

- Pobieranie i filtrowanie danych z publicznych baz danych
- Przetwarzanie danych w Pythonie
- Tworzenie automatycznych pipeline’ów do pracy z dużymi zbiorami danych
- Przygotowanie danych do dalszej analizy lub wizualizacji

---

## Jak uruchomić

1. Sklonuj repozytorium:

bash
```git clone https://github.com/TWOJE_USERNAME/dna_sequence_analysis.git```
```cd dna_sequence_analysis```


2. Zainstaluj wymagane pakiety:

bash
```pip install biopython```


3. Uruchom skrypt:

bash
```python fetch_sequences.py```

Po uruchomieniu w folderze projektu pojawi się plik sekwencje_do_200nt.txt zawierający pobrane i przefiltrowane sekwencje.


## Umiejętności pokazane w tym projekcie

- Praca z Pythonem i zewnętrznymi bibliotekami

- Pobieranie danych z API i publicznych baz danych

- Parsowanie i filtrowanie danych

- Praca z plikami i strukturami danych w Pythonie

- Pisanie czytelnego, modularnego kodu


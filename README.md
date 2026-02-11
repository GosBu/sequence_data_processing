# DNA Sequence Fetcher

## Project description

This project demonstrates how to retrieve biological data in FASTA format from the public GenBank database (NCBI) using Python and the Biopython library.

---

**The goal of the project is to:**

- download DNA sequences based on given identifiers,

- filter sequences by length (up to 200 nucleotides),

- save the results to a file in FASTA format.


The project demonstrates working with external data sources, data processing, and saving outputs in Python.

---

## Technologies and libraries

- **Python 3**

- **Biopython** - for fetching and parsing biological sequences

- **Standard Python modules**: `os`, `datetime` (if needed for file handling and timestamps)

---

## How the code works

1. Setting the user email address – required by NCBI for data retrieval.

2. Defining a list of DNA sequence identifiers (`ids`) from GenBank.

3. Downloading sequences in FASTA format using the `Entrez.efetch` function.

4. Loading sequences into the program using `SeqIO.parse`.

5. Filtering sequences to include only those with a length of up to 200 nucleotides.

6. Closing the connection to the database.

7. Displaying the number of retrieved sequences that meet the length criterion.

8. Saving the results to the file `sekwencje_do_200nt.txt` in FASTA format.

---

## Example applications

- Retrieving and filtering data from public databases

- Data processing in Python

- Building automated pipelines for working with large datasets

- Preparing data for further analysis or visualisation

---

## How to run

1. Clone the repository:

`git clone https://github.com/TWOJE_USERNAME/dna_sequence_analysis.git`
`cd dna_sequence_analysis`


2. Install required packages:

`pip install biopython`


3. Run the script:

`python fetch_sequences.py`


After running the script, the file sekwencje_do_200nt.txt containing the retrieved and filtered sequences will appear in the project folder.

---

## Skills demonstrated in this project:

- Working with Python and external libraries

- Fetching data from APIs and public databases

- Parsing and filtering data

- Working with files and data structures in Python

- Writing clean and modular code


---


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
`git clone https://github.com/TWOJE_USERNAME/dna_sequence_analysis.git`
`cd dna_sequence_analysis`


2. Zainstaluj wymagane pakiety:

bash
`pip install biopython`


3. Uruchom skrypt:

bash
`python fetch_sequences.py`

Po uruchomieniu w folderze projektu pojawi się plik sekwencje_do_200nt.txt zawierający pobrane i przefiltrowane sekwencje.


## Umiejętności pokazane w tym projekcie

- Praca z Pythonem i zewnętrznymi bibliotekami

- Pobieranie danych z API i publicznych baz danych

- Parsowanie i filtrowanie danych

- Praca z plikami i strukturami danych w Pythonie

- Pisanie czytelnego, modularnego kodu


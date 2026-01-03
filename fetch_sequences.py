# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:39:34 2025

@author: magor
"""
# Pobranie 34 sekwencji DNA w formacie FASTA z GenBanku

# Zaimportowanie potrzebnych modułów z biblioteki Biopython
from Bio import Entrez
from Bio import SeqIO

# Ustawienie maila użytkownika
Entrez.email = "magorzata.bujak@gmail.com"

# Zebrane ID sekwencji DNA, które chcę pobrać z GenBanku
ids = ["7157", "1956", "7124", "348", "7422", "3569", "7040", "4524", "2064",	 "3091",
       "2099", "3586",	"351", "1636", "672", "6774", "4318", "1401", "3845", "627",
       "673"	, "9370", "367" , "207",	 "5243", "3123", "4790", "7421", "3553", "1029",
       "5728", "110806262", "1499", "7099", "PQ723210.1", "PQ723205.1", "KX076768.1",
       "MH232730.1", "1MFQ_A", "KX077000.1", "8SKZ_K", "PQ362540.1", "PP953493.1",
       "PP953231.1", "8HAJ_J", "PQ390179.1", "PQ390178.1", "PQ390176.1", " PQ390175.1",
       "PC068158.1", "MH232832.1", "PQ723184.1", "MH232947.1", "KX075422.1"]

# Pobranie sekwencji DNA w formacie FASTA
handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta", retmode="text")

# Wczytanie sekwencji w formacie FASTA
records = SeqIO.parse(handle, "fasta")

# Zapisanie wyników do pliku txt
records_do_200nt = [record for record in records if record.seq[:200]]


# Zakmnięcie wyszukania        
handle.close()
  
# Sprawdź, ile rekordów spełnia warunkek o długoci do 200 nt
print(f"\nZnaleziono {len(records_do_200nt)} sekwencji DNA o długosci do 200 nt.\n")
        
# Zapisanie do pliku tekstowego sekwencji w formacie FASTA
with open("sekwencje_do_200nt.txt", "w") as plik:
    SeqIO.write(records_do_200nt, plik, "fasta")

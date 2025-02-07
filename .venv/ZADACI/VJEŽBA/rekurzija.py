import random

'''1. Napišite funkciju proizvoljnog imena koja prima proizvoljnu pozitivnu cjelobrojnu vrijednost. 
Rezultat je zbroj svih brojeva od 1 do primljene vrijednosti. 
Na primjer, ako funkcija primi vrijednost 5, u pozivajući dio programa mora se vratiti vrijednost 1+2+3+4+5 = 15. 
Ovo je potrebno implementirati pomoću rekurzivne funkcije.'''
def zbroj_rekurzija(broj):
    if broj == 0:
        return 0
    else:
        return broj + zbroj_rekurzija(broj - 1)

br = int(input("Unesite broj:"))
print(zbroj_rekurzija(br))
'''2. Napišite program koji će s tipkovnice učitati jednu proizvoljnu cjelobrojnu vrijednost. 
Za tako učitani cijeli broj prebrojite i ispišite koliko se parnih znamenki nalazi u njemu. 
Prebrojavanje parnih znamenki napravite pomoću rekurzivne funkcije. 
Na primjer, za broj 12345, potrebno je na zaslon ispisati vrijednost 2.'''
def prebroji_parne_rekurzija(unos):
    zadnja_znamenka = unos % 10

    if unos == 0:
        return 0

    if zadnja_znamenka % 2 == 0:
        return 1 + prebroji_parne_rekurzija(unos // 10)
    else:
        return prebroji_parne_rekurzija(unos // 10)

num = int(input("Unesite broj:"))
print("Ima parnih znamenki: ", prebroji_parne_rekurzija(num))

'''3. Napišite bezimenu funkciju koja prima 3 vrijednosti (pretpostavimo da su sve tri vrijednosti pozitivne i strogo veće od 0). 
Ta bezimena funkcija izračunava i vraća rezultat matematičke formule: (a*b + c) / c. 
U glavnom programu ispišite rezultat matematičke formule za sljedeće vrijednosti: a = 5, b = 10; c = 2.'''

a, b, c = 5, 10, 2

bezimenafunkcija = lambda a,b,c : (a*b+c) / c
print(bezimenafunkcija(a,b,c))

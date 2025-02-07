'''
1. Napišite program unutar kojeg ćete u varijablu inicijalizirati listu proizvoljnog sadržaja
(lista od barem 3 vrijednosti). Elemente liste spremite u pojedinačne varijable u jednoj liniji.
Nakon što elemente liste imate spremljene u zasebnim varijablama, ispišite vrijednosti tih varijabli.
'''

lista = [1,2,3]

a=None
b=None
c=None

a,b,c = lista

print(a,b,c)

'''
S tipkovnice učitajte broj proizvoljne vrijednosti. Za tako učitan broj provjerite zadovoljava li on uvjet: 10 <
broj < 30, ako je uvjet zadovoljen, ispišite na ekran: "Zadovoljava!", ako pak uvjet nije zadovoljen, ispišite
na ekran: "Ne zadovoljava!". Ovaj zadatak potrebno je riješiti korištenjem operatora usporedbe, bez
korištenja logičkih operatora i logičkih izraza.
'''

broj = int(input("Unesite broj: "))

if 10 < broj < 30:                   #OPERATORI USPOREDBE SU ==,!=,<,>,<=,>= , A LOGIČKI AND,OR,NOT
    print("Zadovoljava")
else:
    print("Ne zadovoljava")


'''
Implementirajte dvije funkcije. Prva funkcija neka se zove paran() i ona neka ispisuje na ekran: "Paran!",
druga funkcija neka se zove neparan() i ona neka ispisuje na ekran: "Neparan!". S tipkovnice učitajte broj
proizvoljne vrijednosti te pomoću ternarnog operatora detektirajte je li učitana vrijednost parna ili neparna te
ovisno o parnosti pozovite jednu od dviju funkcija koje ste prethodno kreirali.
'''

#SINTAKSA TERNARNOG OPERATORA U PY: vrijednost = rezultat_ako_istina if uvjet else rezultat_ako_nije_istina

def paran():
    print("Paran!")

def neparan():
    print("Neparan!")

uneseni_broj = int(input("Unesite broj: "))

ispis = paran() if uneseni_broj % 2 == 0 else neparan()


'''
Kreirajte listu te ju popunite s 5 proizvoljnih vrijednosti (brojeva). Nakon toga učitajte proizvoljnu vrijednost
(broj) s tipkovnice. Unutar petlje for provjerite nalazi li se vrijednost koju ste učitali s tipkovnice unutar liste.
Ako tražena vrijednost (broj) postoji u listi, ispišite na ekran "Postoji!", u suprotnom ispišite na ekran "Ne
postoji!".
'''

lista2 = [3,6,9,13,33]

provjera_broj = int(input("Unesite broj: "))

if provjera_broj in lista2:
    print("Postoji")
else:
    print("Nepostoji")


'''
Implementirajte funkciju prototipa rezultat(var1, var2), funkcija može primiti dvije vrijednosti. Tako
kreirana funkcija neka u pozivajući dio programa vraća tri vrijednosti dobivene sljedećim aritmetičkim
operacijama: var1*var2, var1+var2, 10*var1+var2. U glavnom dijelu programa pozovite prethodno
implementiranu funkciju te njene povratne vrijednosti spremite u tri zasebne varijable proizvoljnog imena i
ispišite ih.
'''

def rezultat(var1, var2):
    return var1*var2, var1+var2, 10*var1+var2

e,f,g = rezultat(3,4)

print(e,f,g)

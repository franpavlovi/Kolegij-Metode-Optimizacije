'''
Rad s varijablama i listama:

Inicijaliziraj listu s barem tri proizvoljne vrijednosti.
Spremi vrijednosti liste u tri zasebne varijable u jednom retku koda.
Ispiši te varijable.
Zamjena vrijednosti varijabli:
'''

lista = [6,7,9]
a,b,c = lista
print(a,b,c)

'''
Inicijaliziraj dvije varijable s različitim brojevima.
Ispiši njihove vrijednosti, zamijeni ih u jednoj liniji koda, pa ponovno ispiši.
'''

a=5
b= "string"
print("Prije zamjene -",a,b)
a,b = b,a
print("Poslije zamjene -",a,b)

'''
Usporedba s ulančanim operatorima:
Unesi broj s tipkovnice.
Provjeri je li broj između 10 i 30 koristeći ulančane operatore usporedbe (bez logičkih operatora and, or).
Ispiši "Zadovoljava!" ili "Ne zadovoljava!" ovisno o rezultatu.
'''

unos = input("Unesite broj \n")
if 10 < int(unos) < 30:
    print("Zadovoljava!")
else:
    print("Ne zadovoljava!")

'''
Petlje i provjera članstva:
Napravi listu s pet proizvoljnih brojeva.
Unesi broj s tipkovnice i provjeri nalazi li se u listi koristeći for petlju i else dio petlje.
Ispiši "Postoji!" ili "Ne postoji!".
'''
lista2 = [13,23,33,44,50]
brojac = 0

unos2 = int(input("Unesite broj \n"))
for l in lista2:
    if l == unos2:
        brojac=brojac+1

if brojac >= 1:
    print("Postoji!")
else:
    print("Ne postoji")

'''
Ternarni operator:
Unesi broj s tipkovnice.
Pomoću ternarnog operatora ispiši "Paran!" ili "Neparan!" ovisno o parnosti broja.
'''

unos3 = int(input("Unesite broj \n"))

ternarni_operator = print("Paran!") if unos3 % 2 == 0 else print("Neparan!")

'''
Funkcije i ternarni operator:
Implementiraj dvije funkcije: paran() i neparan(), koje ispisuju odgovarajuće poruke.
Unesi broj i pomoću ternarnog operatora pozovi odgovarajuću funkciju ovisno o parnosti.
'''

def paran():
    print("Paran!")

def neparan():
    print("Neparan!")

unos4 = int(input("Unesite broj \n"))

ternarni_operator2 = paran() if unos4 % 2 == 0 else neparan()

'''
Rad s funkcijama i povrat više vrijednosti:
Implementiraj funkciju rezultat(var1, var2) koja vraća tri vrijednosti: proizvod, zbroj, i 10 * var1 + var2.
Pozovi funkciju i ispiši vraćene vrijednosti.
'''

def rezultat(var1, var2):
    return var1 + var2, var1*var2, 10*var1+var2

print(rezultat(10,5))

'''
Rad s nizovima i listama u obrnutom poretku:
Inicijaliziraj string "Hello World!" i listu [1, 2, 3, 4].
Ispiši ih u obrnutom poretku na dva načina: pomoću petlje i pomoću "slice" notacije ([::-1]).
'''

string = "Hello World!"
lista3 = [1,2,3,4]

print(lista3[::-1])
print(string[::-1])
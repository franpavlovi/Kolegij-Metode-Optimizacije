'''REKURZIJA '''
def prebroji_parne(broj):
    if broj == 0:
        return 0

    zadnja_znamenka = broj % 10
    if zadnja_znamenka % 2 == 0:
        return 1 + prebroji_parne(broj // 10)
    else:
        return prebroji_parne(broj // 10)


broj = int(input("Unesite broj: \n"))
rezultat = prebroji_parne(broj)
print(f"Broj parnih znamenki u broju {broj} je: {rezultat}")

''' vanjska funckija izracun() prima dva parametra unutar nje kreirajte parniZbroj() i neparniZbroj()
vracaju matematicke formule, koja ce se pozvati nek se odredi po nekom uvjetu '''
def izracun(a,b):
    def parniZbroj():
        return 2*a+5*b
    def neparniZbroj():
        return a*b-10

    zbroj = a+b

    return parniZbroj() if zbroj % 2 == 0 else neparniZbroj()

print(izracun(3,3))

''' def funkc koja prima 3 vrijednosti , izracunava i vraca rez matematicke formule  .. generirati slucajne brojeve
za parametre fije a,b,c u rasponu od -1000 do 1000, ako nije moguce izvesti racun onda ispsite Err! '''
import random

def racun(c,d,e):
    return (c*d+e) / e

aa = random.randint(-1000,1000)
bb = random.randint(-1000,1000)
cc = random.randint(-1000,1000)

if cc != 0:
    print(racun(aa,bb,cc))
else:
    print("Err!")








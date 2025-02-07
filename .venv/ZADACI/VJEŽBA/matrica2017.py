'''
1. - Generirati matricu A dimenzija (3x3) i matricu B dimenzija (3x4) sa slučajno odabranim brojevima od 0 do 10
- Dopuniti matricu A tricama kako bi dimenzije dviju matrica bile iste
- Zbrojiti matrice A i B, rezultat spremiti u varijablu “rezultat” i svaki element u dobivenoj matrici povećati za 2
- Zbrojiti sve elemente u matrici „rezultat“ i dobivenu varijablu nazvati „suma“
- Kreirati matricu C dimenzija (4x4) u kojoj će svi elementi biti jednaki varijabli „suma“
- Smanjiti sve elemente na dijagonali matrice C za 20
- Kvadrirati sve elemente prvog retka matrice C
- Napomena: Obavezno koristiti naredbe za rad s matricama i rješenje spremiti kao zadatak2.py i pozivati iz naredbenog retka (25 bodova)
-------------------------------------------------------------------------------------------------------------------------------
'''

import numpy as np
import matplotlib.pyplot as plt

matricaA = np.random.randint(0,10, (3,3))
print(matricaA)
print("\n")

matricaB = np.random.randint(0,10, (3,4))
print(matricaB)
print("\n")

#DOPUNJAVANJE MATRICE A
matricaA_dopunjena = np.hstack((matricaA, np.full((3,1), 3))) #HORIZONTAL STACK DODAJEMO STUPCE
print(matricaA_dopunjena)
print("\n")

zbroj_matrica = matricaA_dopunjena + matricaB
print(zbroj_matrica)
print("\n")

zbroj_matrica_povecan_za_2 = zbroj_matrica + 2
print(zbroj_matrica_povecan_za_2)
print("\n")

suma = np.sum(zbroj_matrica_povecan_za_2)
print(suma)
print("\n")

matricaC = np.full((4,4), suma)
print(matricaC)
print("\n")

#GLAVNA DIJAGONALA

np.fill_diagonal(matricaC, np.diag(matricaC) - 20)

print(matricaC)
print("\n")


#KVADRIRANJE ELEMENATA PRVOG REDKA
matricaC[0] = matricaC[0] **2
print(matricaC)
print("\n")
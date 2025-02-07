import numpy as np
import matplotlib.pyplot as plt

'''
matrica1 = np.empty((3,3))
print(matrica1)

matrica2 = np.zeros((3, 3))  # 3x3 matrica popunjena nulama
print(matrica2)

matrica3 = np.ones((3, 3))  # 3x3 matrica popunjena jedinicama
print(matrica3)

matrica4 = np.full((3, 3), 7)  # 3x3 matrica popunjena sa 7
print(matrica4)

rand_matrica = np.random.randint(1, 100, (3, 3))  # 3x3 matrica s cijelim brojevima od 1 do 100
print(rand_matrica)
'''

#Generirati matricu A dimenzija 4x5 sa slučajno odabranim cijelim brojevima od 0 do 100

matricaA = np.random.randint(0,100, (4,5))
print("Matrica A \n", matricaA)

#Potencirati svaki element matrice potencijom 2

A = np.power(matricaA, 2)
print("Matrica A nakon potenciranja na drugu \n", A)

#Generirati matricu B dimenzija 3x5 slučajno odabranim brojevima od 1 do 10

matricaB = np.random.randint(1,10, (3,5))
print("Matrica B \n", matricaB)

#Pomnožiti matricu A i B (dopuniti matricu B nulama kako bi dimenzije dviju matrica bile iste)
B_nadodana = np.vstack([matricaB, np.zeros((2,5))])
print("Matrica B nakon nadopunjavanja \n", B_nadodana)

#Rezultat spremiti u varijablu “rezultat” i svaki element u dobivenoj matrici povećati za 2
rezultat = matricaA @ B_nadodana.T #moramo je transponirati
print("Rezultat mnozenja matrice A i matrice B \n", rezultat)

rezultat_povecano = rezultat + 2
print("Rezultat mnozenja matrice A i matrice B uvecan za 2 \n", rezultat_povecano)

#U prvi redak rezultata postaviti sve nule umjesto postojećih elemenata
rezultat_povecano[0,:] = 0
print("Postavljanje prvog retka na 0-e \n", rezultat_povecano)

#Transponirati dobivenu matricu rezultat
rezultat_povecano = rezultat_povecano.T
print("Transponirana matrica \n", rezultat_povecano)

#U varijablu b spremiti vektor čiji su elementi sume elemenata stupca matrice
suma_stupaca = np.sum(rezultat_povecano, axis=0) #axis=0 SUMA ELEMENATA STUPACA


suma_redaka = np.sum(rezultat_povecano, axis=1) #axis=1 SUMA ELEMENATA REDAKA


#Ispisati dobiveni vektor b
print("Suma elemenata stupaca \n", suma_stupaca)

print("Suma elemenata redaka \n", suma_redaka)

import numpy as np
import matplotlib.pyplot as plt

#GENERIRAJ OVE MATRICE

matricaX = np.array([[10,10,5,10,10],
                     [10,10,5,10,10],
                     [5,5,5,5,5],
                     [10,10,5,10,10],
                     [10,10,5,10,10]])

matricaY = np.array([[8,8,8],
                      [3,3,3],
                      [3,3,3],
                      [8,8,8],
                     [8,8,8]])

#SPOJI IH TAKO DA BUDU DIMENZIJA (5,8)
#spajam ih tako što naslažem jednu na drugu "rame uz rame" komanda hstack - pošto imaju isti broj redaka

matricaZ = np.hstack((matricaX,matricaY))
print(matricaZ)
print("\n")

#DOPUNI MATRICU NULAMA TAKO DA BUDE KVADRATNA

kvadratna_matrica = np.vstack((matricaZ, np.full((3,8), 0)))
print(kvadratna_matrica)
print("\n")

#NA DIJAGONALI MATRICE POMNOŽI SVE ELEMENTE 3 PUTA

np.fill_diagonal(kvadratna_matrica, np.diag(kvadratna_matrica) * 3 )
print(kvadratna_matrica)
print("\n")

#array[start:stop:step] !!!

#SVE ELEMENTE U PARNIM STUPCIMA KVADRIRATI

kvadratna_matrica[:, ::2] = kvadratna_matrica[:, ::2] ** 2

#[:(odaberi svaki redak), :(odaberi sve stupce):2 (ali preskoci svaki drugi)]

print(kvadratna_matrica)
print("\n")

#NA SVE POZICIJE KOJE IMAJU VRIJEDNOST 0 POSTAVITI SUMU TOGA STUPCA


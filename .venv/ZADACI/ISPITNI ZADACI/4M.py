import numpy as np
'''
matricaA = np.random.randint(0,100, (4,5))
print(matricaA)
print("Generirana matrica A \n")

matricaA = np.power(matricaA,2)
print(matricaA)
print("Matrica A potencirana na 2\n")

matricaB = np.random.randint(0,10, (3,5))
print(matricaB)
print("Generirana matrica B \n")

#POMNOZI MATRICE , NADOPUNI MATRICU B NULAMA TAKO DA DIMENZIJE MATRICA BUDU ISTE

matricaB = np.vstack((matricaB, np.full((1,5), 0)))
print(matricaB)
print("Nadopunjena matrica B \n")

#transponiramo matricu B kako bi dobili jednak broj redaka A(4,5) i jednak broj stupaca B^T(5,4)
produktMatrica = matricaA @ matricaB.T
print(produktMatrica)
print("Nova matrica nastala množenjem \n")

#SVAKI ELEMNENT MATRICE POVECATI ZA 2
produktMatrica[:,:] = produktMatrica[:,:] + 2
print(produktMatrica)
print("Svaki element uvecan za 2 \n")

#PRVI REDAK POSTAVITI SVAKI ELEMENT NA 0
produktMatrica[0,:] = produktMatrica[0,:] * 0
print(produktMatrica)
print("Elementi prvog reda postavljeni na 0 \n")

#TRANSPONIRAJ JE
produktMatrica = produktMatrica.T
print(produktMatrica)
print("Transponirana matrica \n")

#U VARIJABLU B SPREMI SPREMI VEKTOR ČIJI SU ELEMENTI SUME ELEMENATA STUPACA MATRICE
b = np.sum(produktMatrica,axis=0)
print(b)
print("Suma stupaca \n")
'''

A = np.array([[10,1,1,1,8],
               [1,10,0,1,8],
               [1,10,10,1,8],
               [1,1,1,10,8],
               [1,1,1,1,10]])

B = np.array([[3,0,0,3],
               [0,3,0,3],
               [0,0,3,3],
               [0,0,0,3]])

#SPREMI SUME ELEMENATA REDAKA MATRICE A
a = np.sum(A, axis=1)
print(a)
print("Suma redaka matrice A \n")

#SPREMI SUME ELEMENATA REDAKA MATRICE B
b = np.sum(B, axis=1)
print(b)
print("Suma redaka matrice B \n")

#ZBROJ VEKRTORE I SPREMI IH U VARIJABLU C
b = np.append(b, 0)
print(b)
print("Nadodani element da vektori budu jednaki \n")

c = a + b
print(c)
print("Novonastali vektor C - zbroj vektora A i B \n")

#KREIRAJ MATRICU C DIMENZIJA 5X5 GDJE SU SVI REDCI JEDNAKI VEKTORU C
C = np.full((5,5), c)
print(C)
print("Matrica C - svaki redak jedank vektoru c \n")

#U PRVI STUPAC MATRICE SVE POSTAVI NA 0
C[:,0] = C[:,0] * 0

#ISPISI DOBIVENU MATRICU C
print(C)
print("Prvi stupac postavljen na 0 \n")








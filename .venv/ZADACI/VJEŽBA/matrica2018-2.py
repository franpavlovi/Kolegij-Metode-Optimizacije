import numpy as np
import matplotlib.pyplot as plt

#(5,5)
matricaX = np.array([[100,100,100,100,10],
                     [100,100,100,10,100],
                     [5,5,5,5,5],
                     [100,10,100,100,100],
                     [10,100,100,100,100],])
#()
matricaY = np.random.randint(0,10, (4,5))

#SPOJI MATRICE TAKO DA BUDU DIMENZIJA (9,5)

matricaZ = np.vstack((matricaX,matricaY))
print(matricaZ)
print("\n")

#SVE ELEMENTE U PARNIM STUPCIMA PODIJELI S 10

matricaZ[:,::2] = matricaZ[:,::2] // 2
print(matricaZ)
print("\n")

#SVE ELEMENTE U NEPARNIM REDCIMA POSTAVITI NA 0

matricaZ[1::2] = matricaZ[1::2] * 0
print(matricaZ)
print("\n")

#DODATI STUPAC ČIJI SU ELEMENTI SUME REDAKA
sume_redaka = np.sum(matricaZ, axis=1)

print("Suma redaka: ",sume_redaka)
print("\n")



matrica_novi_red = np.column_stack([matricaZ, sume_redaka])
print("Matrica Z nakon dodavanja stupca koji je suma redaka", matrica_novi_red)

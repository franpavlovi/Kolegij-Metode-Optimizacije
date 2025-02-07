import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#PRVO DEFINIRAMO FIGURU
plt.figure(figsize=(10,8))

#NASLOV, OGRANIČENJA, IMENA OSI

plt.title("MOJ PRVI GRAF")

plt.xlim(-10,10)
plt.ylim(-10,10)

plt.xlabel("x-os")
plt.ylabel("y-os")

#DEFINIRANJE PODATAKA
x=2
a = np.sin(x) #POJEDINAČNE TOČKE
b = np.cos(x)

y=np.linspace(-10,10,100) #100 TOČKI U INTERVALU OD -10 DO 10
z = y ** 3

ef = np.linspace(-10,10,100)
ef_graf = np.sin(ef)


#PRIKAZ PODATAKA (FUNKCIJA)
plt.plot(x,a, 'ro', label='sin(x)')
plt.plot(x,b, 'ks', label='cos(x)')
plt.plot(y,z, 'b:', label='x^3')
plt.plot(ef,ef_graf, 'r--', label='sin(ef)')


#PRIKAZ LEGENDE
plt.legend()

#PRIKAZ GRAFA
plt.show()



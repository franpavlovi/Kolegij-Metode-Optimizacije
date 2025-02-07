'''
1. Definirati vektor a u intervalu [0,10] s korakom 0.1.
• Definirati vektor b=a2. Na istom grafu (u istom prostoru - figure) nacrtati:
- vektor b (zelenom bojom, crtkana linija) i
- sin(b) (crvenom bojom)
- dodati labele za svaki
- Naslov slike treba biti "Ispitni zadatak"
- naslov x-ose "x-osa" (interval [-1,10])
- i naslov y-ose "y-osa" (interval [-2,9]).
'''

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 1. Definirati vektor a u intervalu [0,10] s korakom 0.1
a = np.arange(0, 10.1, 0.1)

# Definirati vektor b = a^2
b = a ** 2

# Kreiranje figure
plt.figure()

# Crtanje vektora b (zelenom bojom, crtkana linija)
plt.plot(a, b, 'g--', label='b = a^2')

# Crtanje sin(b) (crvenom bojom)
plt.plot(a, np.sin(b), 'r', label='sin(b)')

# Dodavanje oznaka (labela)
plt.xlabel('x-osa')
plt.ylabel('y-osa')

# Postavljanje granica osi
plt.xlim(-1, 10)
plt.ylim(-2, 9)

# Dodavanje naslova
plt.title('Ispitni zadatak')

# Prikaz legende
plt.legend()

# Prikaz grafa
plt.show()


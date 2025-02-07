import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#1.
def izracun(a,b):

    def parniZbroj():
        return 2*a+5*b

    def neparniZbroj():
        return a*b-10

    zbroj = a + b

    return parniZbroj() if zbroj % 2 == 0 else neparniZbroj()

print(izracun(10,6))


#2.
plt.figure()

a = np.arange(0,10.1,0.1)
b = a**3 + a**2 + a

plt.plot(a,b, 'g--', label="b")
plt.plot(a, np.cos(b), 'r-', label="cos(b)")

plt.xlim([-1,10])
plt.ylim([-2,9])

plt.xlabel("x-osa")
plt.ylabel("y-osa")
plt.title("Ispitni zadatak")

plt.legend()
plt.show()


#4.
matricaA = np.random.randint(0,100, (4,5))
print("Kreirana matrica A \n",matricaA)

matricaA = np.power(matricaA,2)
print("Potencirana matrica \n", matricaA)

matricaB = np.random.randint(1,10, (3,5))
print("Matrica B \n",matricaB)

matricaB_dopunjena = np.vstack((matricaB, np.full( (1,5), 0)))
print("Nadopunjena matrica B \n", matricaB_dopunjena)

rezultat = matricaA @ matricaB_dopunjena.T

print("Rezultat množenja matrica \n",rezultat)

rezultat[0,:] = 0
print("Elementi prvog reda postavljeni na 0 \n", rezultat)

rezultat = rezultat.T
print("Transponirna matrica: \n",rezultat)

b = np.sum(rezultat, axis=0)
print("Vektor sume stupaca", b)





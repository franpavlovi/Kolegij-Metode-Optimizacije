import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

'''
#1.
plt.figure()

a = np.arange(1,10,0.1)
b = a**3 + a**2 + a

plt.plot(a,b, 'g--', label="vektor b")
plt.plot(a, np.cos(b), 'r-', label="vektor cos(b)")

plt.title("ispitni zadatak")
plt.xlabel("x-osa")
plt.ylabel("y-osa")

plt.xlim(-1,10)
plt.ylim(-2,9)

plt.legend()
plt.show()
'''

'''
#2.
plt.figure()

a = np.arange(-10,10,0.1)
b = a**2

plt.plot(a,b, 'g--', label="x^2")
plt.plot(a, np.sin(b), 'r-', label="cos(b)")

plt.title("ispitni zadatak")

plt.xlim(-1,10)
plt.ylim(-2,9)

plt.xlabel("x-osa")
plt.ylabel("y-osa")

plt.legend()
plt.show()
'''
'''
#3.
plt.figure()

a = np.arange(0,10,0.1)
b = a**4

plt.xlim(-1,10)
plt.ylim(-2,9)

plt.title("ispitni zadatak")
plt.xlabel("x-osa")
plt.ylabel("y-osa")

plt.plot(a,b,'r-', label="x^4")

plt.plot(a, np.sin(b),'g-', label="sin(b)")

plt.plot(a, np.cos(b), 'y-', label="cos(b)")

plt.legend()
plt.show()
'''

#4.
plt.figure()

a = np.arange(-10,10,0.1)
b = a**2

plt.xlim(-10,10)
plt.ylim(-10,9)

plt.xlabel("x-osa")
plt.ylabel("y-osa")

plt.title("ispitni zadatak")

plt.plot(a,b, 'r-', label="x^2")

plt.plot(a, np.sin(b), 'k-', label="sin(b)")

plt.legend()
plt.show()
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



#DEFINIRAJ VELICINU FIGURE
plt.figure(figsize=(10,8))

#DEFINIRAJ PODATKE
x = np.linspace(-10,10,100)
a = x ** 2

y = np.linspace(-10,10,100)
b = -x ** 2

#CRTANJE PRVOG GRAFA ---- RADI SE POMOĆU PLT.SUBPLOT
plt.subplot(2,3,1) #3 redka, 1 stupac i 1. graf

plt.xlim(-10,10)
plt.ylim(-10,20)
plt.title(" Prvi graf - x^2")

plt.plot(x,a, 'r-', label='x^2')
plt.legend()


#CRTANJE DRUGOG GRAFA
plt.subplot(2,3,4)

plt.xlim(-10,10)
plt.ylim(-20,5)
plt.title(" Drugi graf - -x^2")

plt.plot(y,b, 'r-', label='x^2')
plt.legend()


#CRTANJE TRECEG GRAFA
plt.subplot(1,2,2)

plt.xlim(-10,10)
plt.ylim(-20,20)
plt.title("Treći graf - zajednički")

plt.xlabel("x-os")
plt.ylabel("y-os")

plt.plot(x,a,'r--', label='x^2')
plt.plot(y,b,'b--', label='-x^2')

plt.tight_layout()
plt.legend()
plt.show()
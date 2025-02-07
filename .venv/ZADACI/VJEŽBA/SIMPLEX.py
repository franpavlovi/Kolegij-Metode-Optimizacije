from scipy.optimize import linprog
import numpy as np
'''
# Koeficijenti funkcije cilja (negativni jer linprog minimizira po defaultu)
c = [-3, -5]

# Ograničenja (lijeva strana nejednakosti)
A = [
    [2, 3],   # 2x + 3y <= 8
    [1, 1]    # x + y <= 4
]

# Desna strana ograničenja
b = [8, 4]

x_bounds = (0, None)
y_bounds = (0, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

# Prikaz rezultata
print("Optimalna vrednost funkcije cilja (Z):", -result.fun)
print("Vrednosti promenljivih:")
print("x =", result.x[0])
print("y =", result.x[1])
'''
'''
#FCILJA
c = [-13, -11]
#LIJEVA STRANA OGRANICENJA
a = [[2.5,1.5],
     [1/60,1/30],
     [0.4,0.5]]
#DESNA STRANA OGRANICENJA
b = [787.5, 7, 160]

x_bounds = (0, None)
y_bounds = (0, None)

rezultat = linprog(c, A_ub=a, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

print("Optimalna vrednost funkcije cilja (Z):", -rezultat.fun)
print("Vrednosti promenljivih:")
print("x =", rezultat.x[0])
print("y =", rezultat.x[1])
'''

#PRIMJER SA PRVOG KOLOKVIJA (KAD SMO RUČNO RADILI SIMPLEX)

c = [-2,-4,7]
a = [[3,2,-1],[1,-2,0]]
b = [4,3]

x_bounds = (0, None)
y_bounds = (0, None)
z_bounds = (0, None)

rezultat = linprog(c, A_ub=a, b_ub=b, bounds=[x_bounds, y_bounds, z_bounds], method='simplex')
print("Maksiminzirana vrijednost: ", -rezultat.fun)
print("Vrijednost x: ",rezultat.x[0])
print("Vrijednost y: ", rezultat.x[1])


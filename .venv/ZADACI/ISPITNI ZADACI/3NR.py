import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Newton-Raphson method implementation
def newtonRaphson(f, g, x0, e=1e-6, N=100):
    print("\n\n *** NEWTON RAPHSON METHOD IMPLEMENTATION ***")
    steps = []
    roots = []
    step = 1
    condition = True

    while condition:
        if g(x0) == 0.0:
            print("Divide by zero error! Stopping iteration.")
            break

        x1 = x0 - f(x0) / g(x0)
        steps.append(step)
        roots.append(x1)
        print(f"Iteration-{step}, x1 = {x1:.6f} and f(x1) = {f(x1):.6f}")

        if step > N:
            print("\nNot Convergent within maximum iterations.")
            break

        if abs(f(x1)) <= e:
            print(f"\nConverged to root: {x1:.8f}")
            break

        x0 = x1
        step += 1

    return steps, roots

# Function 1
f1 = lambda x: x**5 + 2*x**3 + 3*x**2 + np.cos(x)
g1 = lambda x: 5*x**4 + 6*x**2 + 6*x - np.sin(x)
interval1 = (-2, 0)
x0_1 = (interval1[0] + interval1[1]) / 2
e = 1e-6
N = 100
print("\n\n*** Function 1 ***")
steps1, roots1 = newtonRaphson(f1, g1, x0_1, e, N)

x = np.linspace(interval1[0], interval1[1], 500)
y = f1(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Function 1", color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.scatter(roots1, [f1(r) for r in roots1], color='red', label='Newton-Raphson Iterations')
plt.title("Newton-Raphson Method Visualization - Function 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()
plt.show()

# Function 2
f2 = lambda x: 3*x**5 + 8*x**4 - 24*x**2 - 13*x
g2 = lambda x: 15*x**4 + 32*x**3 - 48*x - 13
interval2 = (0, 3)
x0_2 = (interval2[0] + interval2[1]) / 2
print("\n\n*** Function 2 ***")
steps2, roots2 = newtonRaphson(f2, g2, x0_2, e, N)

x = np.linspace(interval2[0], interval2[1], 500)
y = f2(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Function 2", color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.scatter(roots2, [f2(r) for r in roots2], color='red', label='Newton-Raphson Iterations')
plt.title("Newton-Raphson Method Visualization - Function 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()
plt.show()

# Function 3
f3 = lambda x: 2*x**4 - x**3 + np.sin(x)
g3 = lambda x: 8*x**3 - 3*x**2 + np.cos(x)
interval3 = (-3, 3)
x0_3 = (interval3[0] + interval3[1]) / 2
print("\n\n*** Function 3 ***")
steps3, roots3 = newtonRaphson(f3, g3, x0_3, e, N)

x = np.linspace(interval3[0], interval3[1], 500)
y = f3(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Function 3", color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.scatter(roots3, [f3(r) for r in roots3], color='red', label='Newton-Raphson Iterations')
plt.title("Newton-Raphson Method Visualization - Function 3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()
plt.show()

# Function 4
f4 = lambda x: 2*x**4 - x**3 + 4*x
g4 = lambda x: 8*x**3 - 3*x**2 + 4
interval4 = (-3, 3)
x0_4 = (interval4[0] + interval4[1]) / 2
print("\n\n*** Function 4 ***")
steps4, roots4 = newtonRaphson(f4, g4, x0_4, e, N)

x = np.linspace(interval4[0], interval4[1], 500)
y = f4(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Function 4", color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.scatter(roots4, [f4(r) for r in roots4], color='red', label='Newton-Raphson Iterations')
plt.title("Newton-Raphson Method Visualization - Function 4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()
plt.show()
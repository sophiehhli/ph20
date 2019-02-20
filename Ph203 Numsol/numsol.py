import numpy as np 
import matplotlib.pyplot as plt

# ------ EXPLICIT METHOD ------

# Parameters
h = 0.004
x0 = 2
v0 = 2
t0 = 0 
N = 50000

# Explicit Eurler Method
n = np.arange(N)
t = t0 + n * h

x = np.zeros(N)
v = np.zeros(N)

x[0] = x0
v[0] = v0

for i in range(N-1): 
	x[i+1] = x[i] + v[i] * h 
	v[i+1] = v[i] - x[i] * h

plt.plot(t, x, label='displacement(x)')
plt.plot(t, v, label='velocity(v)')
plt.legend()
plt.xlabel('t')
plt.show()

# Comparison to Analytic
x_analytic  = x0 * np.cos(t) + v0 * np.sin(t)
v_analytic = -1 * x0 * np.sin(t) + v0 * np.cos(t)

plt.plot(t,x)
plt.plot(t, x_analytic)
plt.plot(t, v_analytic)
plt.show()

# Global Errors 
x_gerror = x_analytic - x 
v_gerror = v_analytic - v

plt.plot(t, x_gerror, label='Displacement(x)')
plt.plot(t, v_gerror, label='Velocity(v)')
plt.legend()
plt.xlabel('t')
plt.ylabel('Global Error')
plt.show()

# Evolution of total Energy
E = x**2 + v**2
plt.plot(t, E)
plt.title('Evolution of Normalized Total Energy')
plt.xlabel('t')
plt.ylabel('E')
plt.show()

# Phase Space
plt.plot(x,v)
plt.plot(x_analytic,v_analytic)
plt.xlabel('Displacement (x)')
plt.ylabel('Velocity (x)')
plt.title('Phase-space of the explicit Euler mehtod')
plt.show()
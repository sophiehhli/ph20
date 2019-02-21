import numpy as np 
import matplotlib.pyplot as plt
import sys
# ------ TRUNCATION ERROR -------

def gerror(h,x0,v0,t0,N): 
	n = np.arange(N)
	t = t0 + n * h

	x = np.zeros(N)
	v = np.zeros(N)

	x[0] = x0
	v[0] = v0

	for i in range(N-1): 
		x[i+1] = x[i] + v[i] * h 

	x_analytic  = x0 * np.cos(t) + v0 * np.sin(t)
	return x_analytic - x

t_error = np.zeros(5)

h0 = 0.0001
N0 = 100
t_error[0] = np.max(gerror(h0, 2, 2, 0, N0))
t_error[1] = np.max(gerror(h0/2, 2, 2, 0, N0))
t_error[2] = np.max(gerror(h0/4, 2, 2, 0, N0))
t_error[3] = np.max(gerror(h0/8, 2, 2, 0, N0))
t_error[4] = np.max(gerror(h0/16, 2, 2, 0, N0))

# Plot 
h_plt = np.array([h0, h0/2, h0/4, h0/8, h0/16])

plt.plot(h_plt, t_error)
plt.xlabel('h')
plt.ylabel('Truncation Error')
plt.savefig('Images/truncerror.png')

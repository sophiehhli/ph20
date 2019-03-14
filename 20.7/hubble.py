import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import optimize
from scipy import integrate

data = np.genfromtxt('SCPUnion2.1_mu_vs_z.txt', comments='#', delimiter='	')
distmod = data[:,2]
distmoderr = data[:,3]
lumdist = (10**((distmod/5)+1))/(10**6)
lumdisterr = (np.log(10)/5)*(lumdist)*distmoderr
redshift = data[:,1]

# Initial Data Plotting ------------------------------------------------------------------------------------------------
plt.errorbar(redshift,distmod,yerr =distmoderr,fmt='.',lw =0.3, elinewidth = 0.3, ecolor = 'g')
plt.xlabel('Redshift')
plt.ylabel('Distance Modulus')
plt.show()
plt.errorbar(redshift,lumdist,yerr =lumdisterr,fmt='.',lw =0.3, elinewidth = 0.3, ecolor = 'g')
plt.xlabel('Redshift')
plt.ylabel('Luminosity Distance (Mpc)')
plt.show()

# Linear Fit Plotting -----------------------------------------------------------------------------------------------
lowrs = []
lowrslumdist =[]
lowrslumdisterr = []

for i in range(len(redshift)):
	if redshift[i] < 0.05:
		lowrs.append(redshift[i])
		lowrslumdist.append(lumdist[i])
		lowrslumdisterr.append(lumdisterr[i])

def linhubble(x,g): 
	return g*x

param = optimize.curve_fit(linhubble, lowrs, lowrslumdist)
g = param[0][0]
H0 = 299792.458/g

plt.plot(redshift, linhubble(redshift, param[0]), label='Linear Fit', color ='r', linewidth = 1)
plt.errorbar(redshift,lumdist, yerr = lumdisterr,fmt='.',lw =0.3, elinewidth = 0.3, ecolor = 'g',label='Data')
plt.xlabel('Redshift')
plt.ylabel('Luminosity Distance (Mpc)')
plt.show()

# Non Linear Fit Plotting ----------------------------------------------------------------------------------------------------
def nonlinhubble(x,g,q): 
	return g*x*(1+((1-q)/2)*x)

paramnl = optimize.curve_fit(nonlinhubble, redshift, lumdist)

H0nl = 299792.458/paramnl[0][0]
q = paramnl[0][1]
rslinspace = np.linspace(0, 1.5, num=580)

plt.plot(rslinspace, nonlinhubble(rslinspace, paramnl[0][0], q), label='Linear Fit', color ='r', linewidth = 1)
plt.errorbar(redshift,lumdist, yerr = lumdisterr,fmt='.',lw =0.3, elinewidth = 0.3, ecolor = 'g',label='Data')
plt.xlabel('Redshift')
plt.ylabel('Luminosity Distance (Mpc)')
plt.show()

# FLRW ----------------------------------------------------------------------------------------------------------------
def flrw(x,g,om):
	integrand = 1/np.sqrt(((1+x)**3)*om+(1-om))
	return g*integrate.cumtrapz(integrand, x=x, initial = 0)*(1+x)

paramflrw = optimize.curve_fit(flrw, redshift, lumdist)
H0flrw = 299792.458/paramflrw[0][0]
om = paramflrw[0][1]

print(H0flrw)
print(om)

plt.plot(rslinspace, nonlinhubble(rslinspace, paramflrw[0][0], om), label='Linear Fit', color ='r', linewidth = 1)
plt.errorbar(redshift,lumdist, yerr = lumdisterr,fmt='.',lw =0.3, elinewidth = 0.3, ecolor = 'g',label='Data')
plt.xlabel('Redshift')
plt.ylabel('Luminosity Distance (Mpc')
plt.show()

print(om)
error = np.sqrt(paramflrw[1][1][1])
print("sig squared:  " + str(paramflrw[1][1][1]))
sigma =(1-om)/error
print(sigma)
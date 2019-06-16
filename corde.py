import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

n = 100
Ltot = 50
L=Ltot/n
g = 9.81
ro = 1000
Vitesse = 3
Msonar = 9

D = 6.3 * 10**-3
Ssonar = np.pi*0.03**2
Vsonar = Ssonar*0.85
Vcable = L*np.pi * (6.3/2 * 10**(-3))**2
Mcable = Vcable*2700
Cp = 1.1
Cf = 0.012
C = 0.6








F0 = np.sqrt((Msonar*g - Vsonar*ro*g)**2 + (0.5*ro*C*Ssonar*Vitesse**2)**2)
alpha0 = np.arctan((Msonar*g-Vsonar*ro*g)/(0.5*ro*C*Ssonar*Vitesse**2))
beta0 = alpha0

print((Msonar*g - Vsonar*ro*g)**2 )
print((0.5*ro*C*Ssonar*Vitesse**2)**2)
print(F0)

Fliste = [F0]
aliste = [alpha0]
bliste= [beta0]

Fn = F0
alphan = alpha0
beta0 = 1

for k in range(n):
    def f(b):
        return -L/4*ro*Cp*D*L*Vitesse**2*(np.cos(b))**2-L/2*np.cos(b)*(Vcable*ro*g-Mcable*g)-L/2*np.sin(b)*Fn*np.cos(alphan) + L/2*np.cos(b)*Fn*np.sin(alphan)

    betan = fsolve(f, 2)
    Tn = 0.5 * ro * Cp * D * L * Vitesse ** 2 * np.cos(betan) ** 2
    Tt = 0.5 * ro * Cf * np.pi * D * L * Vitesse ** 2 * np.sin(betan) ** 2
    Fn, alphan = np.sqrt((-Fn*np.cos(alphan) + Tn*np.sin(betan) - Tt*np.cos(betan))**2 + (-Fn*np.sin(alphan) - ro*Vsonar*g + Msonar*g - Tn*np.cos(betan) - Tt*np.sin(betan))**2), np.arctan((-Fn*np.sin(alphan) - ro*Vsonar*g + Msonar*g - Tn*np.cos(betan) - Tt*np.sin(betan))/(-Fn*np.cos(alphan) + Tn*np.sin(betan) - Tt*np.cos(betan)))
    Fliste.append(Fn)
    aliste.append(alphan)
    bliste.append(betan)


abs1 = 0
ord1 = 0
for k in range(n):
    print(bliste[k])
    abs1 += abs(L*np.cos(bliste[k+1]))
    ord1 += abs(L*np.sin(bliste[k+1]))
    plt.scatter(abs1, ord1)
plt.axis('equal')
plt.show()


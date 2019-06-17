import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math
n = 50
Ltot = 50
L=Ltot/n
g = 9.81
ro = 1000
Vitesse = 2.5
Msonar = 9

D = 6.3 * 10**-3
Ssonar = np.pi*0.03**2
Vsonar = Ssonar*0.85
Vcable = L*np.pi * (6.3/2 * 10**(-3))**2
Mcable = Vcable*1450
Cp = 1.2
Cf = 0.012
C = 0.6


F0x = 0.5*ro*(C*Ssonar+Cf*np.pi*0.06*0.85)*Vitesse**2
F0y = (Msonar - ro*Vsonar)*g
print(F0x)
Fx = F0x
Fy = F0y

liste_beta = []


def f(b):
    return -0.25 * L * ro * Cp * D * L * Vitesse ** 2 * (np.cos(b)) ** 2 - L * Fx * np.sin(b) + L * Fy * np.cos(
        b) + 0.5 * L * (Msonar - ro * Vsonar) * g * np.cos(b)
betan = fsolve(f, 1.57)

liste_beta.append(betan)

for k in range(n-1):
    def f(b):
        return -0.25*L*ro*Cp*D*L*Vitesse**2*(np.sin(b))**2 - L*Fx*np.sin(b) + L*Fy*np.cos(b) + 0.5*L*(Mcable - ro*Vcable)*g*np.cos(b)
    betan = fsolve(f, betan)
    Tn = 0.5 * ro * Cp * D * L * Vitesse ** 2 * (np.sin(betan)) ** 2
    Tt = 0.5 * ro * Cf * np.pi * D * L * Vitesse ** 2 * (np.cos(betan)) ** 2
    Fx = Fx + Tt*np.cos(betan) + Tn*np.sin(betan)
    Fy = Fy + (Mcable - ro*Vcable)*g + Tt*np.sin(betan) -Tn*np.cos(betan)
    liste_beta.append(betan)

abs1 = 0
ord1 = 0

for k in range(n):
    print(liste_beta[k])
    abs1 += L*np.cos(liste_beta[k])
    ord1 += L*np.sin(liste_beta[k])
    plt.scatter(abs1, ord1)
plt.axis('equal')
plt.show()
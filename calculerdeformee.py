import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math





n = 50
Ltot = 50
L=Ltot/n
g = 9.81
ro = 1000

Msonar = 9

D = 6.3 * 10**-3
Ssonar = np.pi*0.03**2
Vsonar = Ssonar*0.85
Vcable = L*np.pi * (6.3/2 * 10**(-3))**2
Mcable = Vcable*1450
Cp = 1.2
Cf = 0.012
C = 0.6

def tracer(Vitesse):

   F0x = 0.5*ro*(C*Ssonar+Cf*np.pi*0.06*0.85)*Vitesse**2
   F0y = (Msonar - ro*Vsonar)*g




   Fx = F0x
   Fy = F0y

   liste_beta = []


   def f(b):
       return -0.25 * L * ro * Cp * D * L * Vitesse ** 2 * (np.sin(b)) ** 2 - L * Fx * np.sin(b) + L * Fy * np.cos(
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

   #print("F ", np.sqrt(Fx**2 + Fy**2))

   abs1 = 0
   ord1 = 0
   X = []
   Y = []


   for k in range(n):
       
       abs1 += L*np.cos(liste_beta[k])
       abs2 = abs1
       ord1 += L*np.sin(liste_beta[k])
       X.append(abs1[0])
       Y.append(ord1[0])
   return (X,Y)


Liste_Vitesse = [0.257,0.514,0.772,1.028,1.543,2.572]
for Vitesse in Liste_Vitesse:

   X = tracer(Vitesse)[0]
   Y = tracer(Vitesse)[1]

   X1 = np.array(X) - np.ones(len(X))*X[-1]
   Y1 = np.array(Y) - np.ones(len(Y))*Y[-1]
   plt.plot(X1, Y1,label="v = " + str(round(Vitesse*1.94,1)) + " noeuds")

   print("Pour la vitesse " + str(Vitesse*1.94) + " noeuds " + "le layback est de " + str(np.abs(X[-1])) + " mètres")
   


plt.axis('equal')

plt.title("Déformée du câble de 50 m en fonction de la vitesse du courant")
plt.grid()
plt.legend()

plt.show()
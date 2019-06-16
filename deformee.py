import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt




n = 100
g = 9.81 
rho_eau = 1000
v = 1e-6
L = 100
l = L/n
D = 6.3e-3
rho_cable = 500
m = 9 
C_sonar = 0.5
S_sonar = (3e-2)**2*np.pi 
C_cable = 1.1
V = l*(D*0.5)**2*np.pi
Vsonar = S_sonar*1
Tt = 1
Tn = 1

P = 1
Archi = rho_eau*D**2*3.1415*l*g
Poid =  rho_cable*D**2*3.1415*l*g


# Force du sonar sur le cable.

F = np.sqrt((m*g - Vsonar*rho_eau*g)**2 + (0.5*rho_eau*C_sonar*S_sonar*v**2)**2)

alpha = np.arctan((m*g - Vsonar*rho_eau*g)/(0.5*rho_eau*C_sonar*S_sonar*v**2))

beta = alpha

print("F vaut:    " + str(F) + " N")
print("Alpha vaut:    " + str(alpha) + " rad")

S = [[F,alpha,beta]]



def myFunction(z):
   

   # inconnue au rang n

   f = z[0]
   a = z[1]
   b = z[2]

   

   
   
   
   # Forces de Trainée


   Tn = 0.5*rho_eau*C_cable*D*l*v**2*(np.cos(b))**2
   Tt = 0.5*rho_eau*C_cable*D*l*v**2*(np.sin(b))**2*np.pi

   F = np.empty(3)

   # Trois équations issues du PFS et du TMD 
   
   F[0] =  f*np.sin(a - b) - f_1*np.sin(a_1 - b_1) # TMD
   F[1] = +np.cos(a - b)*f - np.cos(+a_1 - b_1)*f_1 + Tt +   (-Poid + Archi)*np.sin(b_1) # PFS sur la tangente

   F[2] =f*np.sin(a - b) + f_1*np.sin(a_1 - b_1) + Tn + (-Poid + Archi)*np.cos(b_1) # PFS sur la normale
   
   return F





for i in range(n):
   # solution au rang n -1 


   f_1 = S[i][0]
   a_1 = S[i][1]
   b_1 = S[i][2]
   

   zGuess = S[-1] # Je prend le rend n-1 comme solution approximative
   z = fsolve(myFunction,zGuess)
   


   S.append(z)
   #print(S)   




X = []
Y = []
x = 0
y = 0
for  i in range(len(S)):
   cos = np.cos(S[i][2])
   sin = np.sin(S[i][2])
   x += l*cos
   y += l*sin 
   X.append(x) 
   Y.append(y)

plt.figure()

plt.plot(X,Y)
plt.show()
 
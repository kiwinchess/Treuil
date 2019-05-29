
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt

L=1
PI=5
P=10
ro=1000
Cp=10
D=0.0063
L=1
V=3
Fn=20
an=0

def f(x):
    return L/2*np.cos(x)*(PI-P)+L/4*ro*Cp*D*L*V*V*np.cos(x)**2-L*Fn*(np.cos(x)*np.sin(an)-np.cos(an)*np.sin(x))


y = op.fsolve(f,1)
print(y)

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:28:47 2020

@author: B00741681
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000

x = np.linspace(-1, 1, N)
"""
y = np.zeros((N))
y[x>-0.25] = 1

y[x>0.25] = 0
"""

y = (1.0 - abs(x))**2


# additive gaussian noise
y = y + np.random.randn(N) * 0.0

#polynomial order
pord = 155


# U matrix init
U = np.zeros((N, pord+1))


# U matrix accumulation for polynomial fitting
for i in range(pord+1):
    U[:, i] = x**i



"""
# U matrix accumulation Chebyshev orthogonal polynomials
for i in range(pord+1):
    if i == 0:
        U[:, i] = 1.0
    elif i == 1:
        U[:, i] = x
    else:
        U[:, i] = 2.0 * x * U[:, i-1] - U[:, i-2]
"""
   
  
# Rx = U^H * U  
Rx =  np.matmul(np.transpose(np.conjugate(U)), U)    

# ry = U^H * y
ry =  np.matmul(np.transpose(np.conjugate(U)), y) 

# a = RX^-1 * ry
a = np.matmul(np.linalg.inv(Rx), ry)    
   
# z = U * a
z = np.matmul(U, a) 


plt.figure()
plt.plot(x, y, x, z)
plt.show()

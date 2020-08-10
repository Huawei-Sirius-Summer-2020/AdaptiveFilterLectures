# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:32:51 2020

@author: bakhu
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.load('data/lte_2c_data0_in.npy')
y = np.load('data/lte_2c_data0_out.npy')

d = y - x

ORD = 7

dl = [-2, -1, 0, 1, 2]
ds = [-2, -1, 0, 1, 2]

mem = len(dl)

U = np.zeros((len(d), mem*(ORD+1)), dtype = complex)


ind = np.arange(2,len(d)-2)
for k in ind:
    for m in range(mem):
        for p in range(ORD+1):
            U[k, p+m*(ORD+1) ] = x[k - dl[m]] * abs(x[k - ds[m]])**(2*p)
        
        
# LS estimation
     
Rxx = np.matmul(np.conj(U.T), U)
rdy = np.matmul(np.conj(U.T), d)

w = np.matmul(np.linalg.pinv(Rxx),rdy)

z = np.matmul(U, w)


plt.figure(1)
plt.psd(x, NFFT = 2048)
plt.psd(d, NFFT = 2048)
plt.psd(z, NFFT = 2048)
plt.psd(d-z, NFFT = 2048)
plt.grid(True)
plt.show()
        

plt.figure(2)
plt.plot(abs(x))
plt.plot(abs(d))
plt.plot(abs(z))
plt.plot(abs(d-z))

    
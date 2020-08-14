
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:32:51 2020

@author: bakhu
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.load('data/lte_10c_data0_in.npy')
y = np.load('data/lte_10c_data0_out.npy')

d = y - x

P = 3

dl = [ -1, 0, 1]
ds = [ -1, 0, 1]

M = len(dl)
N = len(d)

U = np.zeros((N, M*(P+1)), dtype = complex)


ind = np.arange(1,N-1)
for k in ind:
    for m in range(M):
        for p in range(P+1):
            U[k, p+m*(P+1) ] = x[k - dl[m]] * abs(x[k - ds[m]])**(p)
        
        
# LS estimation
     
Rxx = np.matmul(np.conj(U.T), U)
rxd = np.matmul(np.conj(U.T), d)

w = np.matmul(np.linalg.pinv(Rxx), rxd)

z = np.matmul(U, w)


plt.figure()
plt.psd(x, NFFT = 2048)
plt.psd(d, NFFT = 2048)
plt.psd(z, NFFT = 2048)
plt.psd(d-z, NFFT = 2048)
plt.grid(True)
plt.show()
        

plt.figure()
plt.plot(abs(x))
plt.plot(abs(d))
plt.plot(abs(z))
plt.plot(abs(d-z))

    
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

ORD = 9

U = np.zeros((len(d), ORD+1), dtype = complex)

for k in range(len(d)):
    for p in range(ORD+1):
        U[k, p] = x[k] * abs(x[k])**p
        
        
# LS estimation
        
Rxx = np.matmul(np.conj(U.T), U)
rdy = np.matmul(np.conj(U.T), d)

w = np.matmul(np.linalg.pinv(Rxx),rdy)

z = np.matmul(U, w)


plt.figure(1)
plt.psd(x, NFFT = 2048)
plt.psd(d, NFFT = 2048)
plt.psd(d-z, NFFT = 2048)
plt.grid(True)
plt.show()
        
    
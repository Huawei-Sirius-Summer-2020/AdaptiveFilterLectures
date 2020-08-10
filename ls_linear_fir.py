# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:54:23 2020

@author: B00741681
"""

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

x = np.load('data/linear_lte_2c_data0_in.npy')
y = np.load('data/linear_lte_2c_data0_out.npy')
d = y - x




M = 7

D = 3 


N = len(x)

U = np.zeros((N, M), dtype = complex)



for i in range(D, N-D):
    U[i, :] = x[(i-D):(i+D)+1]
    
    


Rxx = np.matmul(np.conj(U.T), U)
rxd = np.matmul(np.conj(U.T), d)

w = np.matmul( np.linalg.pinv(Rxx + np.eye(M)*100), rxd)

z = np.matmul(U, w)

plt.figure()
plt.psd(x, 2048)
plt.psd(y, 2048)
plt.psd(d, 2048)
plt.psd(z, 2048)
plt.psd(d-z, 2048)
plt.show()
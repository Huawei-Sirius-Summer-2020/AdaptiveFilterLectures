# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:32:06 2020

"""


import numpy as np
import matplotlib.pyplot as plt

N = 500

x = np.random.randn(N) + 1j*np.random.randn(N)

rxx = np.zeros(2*N+51, dtype = 'complex')
qxx = np.zeros(2*N+51, dtype = 'complex')

for m in range(N):
    ind = np.arange(0, N-m-1, 1, dtype = 'int') 
    rxx[m+N+25] = np.sum(x[ind+m]*np.conj(x[ind]))/(N-m)
    qxx[m+N+25] = np.sum(x[ind+m]*np.conj(x[ind]))/N
    
    
for m in np.arange(-N+1, -1, 1):
    ind = np.arange(0, N+m-1, 1, dtype = 'int')
    rxx[m+N+25] = np.sum(np.conj(x[ind-m])*x[ind])/(N+m)    
    qxx[m+N+25] = np.sum(np.conj(x[ind-m])*x[ind])/N  
    
m = np.arange(-N-25, N+26, 1)    

plt.figure(1)
plt.plot(m, np.real(rxx), m, np.imag(rxx)) 
plt.xlim(-N-25,N+25)
plt.ylim(-1,2.5)
plt.show   
    

plt.figure(2)
plt.plot(m, np.real(qxx), m, np.imag(qxx)) 
plt.xlim(-N-25,N+25)
plt.ylim(-1,2.5)
plt.show   


    
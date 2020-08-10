# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:22:29 2020

@author: B00741681
"""

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
"""
x = np.load('data/gsm_4c_in.npy')
y = np.load('data/gsm_4c_out.npy')
e = y - x

plt.figure()
plt.psd(x, 2048)
plt.psd(y, 2048)
plt.psd(e, 2048)
plt.show()



x = np.load('data/linear_lte_2c_data0_in.npy')
y = np.load('data/linear_lte_2c_data0_out.npy')
e = y - x

plt.figure()
plt.psd(x, 2048)
plt.psd(y, 2048)
plt.psd(e, 2048)
plt.show()


x = np.load('data/lte_2c_data0_in.npy')
y = np.load('data/lte_2c_data0_out.npy')
e = y - x

plt.figure()
plt.psd(x, 2048)
plt.psd(y, 2048)
plt.psd(e, 2048)


x = np.load('data/lte_10c_data0_in.npy')
y = np.load('data/lte_10c_data0_out.npy')
e = y - x

plt.figure()
plt.psd(x, 2048)
plt.psd(y, 2048)
plt.psd(e, 2048)
plt.show()

"""
x = np.load('data/lte_4c_data0_in.npy')
y = np.load('data/lte_4c_data0_out.npy')
e = y - x

plt.figure()
plt.psd(x, 2048)
plt.psd(y, 2048)
plt.psd(e, 2048)
plt.psd(z, 2048)
plt.show()

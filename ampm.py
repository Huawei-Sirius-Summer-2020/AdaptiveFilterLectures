# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.load('data/gsm_4c_in.npy')
y = np.load('data/gsm_4c_out.npy')

#AM - PM
phi = 180.0 * np.angle(np.conj(x)*y) / np.pi 
plt.figure()
plt.scatter(np.abs(x), phi, s = 0.1)
plt.xlabel("|x(n)|")
plt.ylabel("angle(x,y), degree")
plt.title("AM-PM")
plt.grid(True)
plt.show()
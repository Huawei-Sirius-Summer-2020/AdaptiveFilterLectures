# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.load('data/gsm_4c_in.npy')
y = np.load('data/gsm_4c_out.npy')

#AM - AM
plt.figure()
plt.scatter(np.abs(x), np.abs(y), s = 0.1)
plt.xlabel("|x(n)|")
plt.ylabel("|y(n)|")
plt.title("AM-AM")
plt.grid(True)
plt.show()

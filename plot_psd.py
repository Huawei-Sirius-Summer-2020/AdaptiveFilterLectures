# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.load('data/gsm_4c_in.npy')
y = np.load('data/gsm_4c_out.npy')

d = y - x

plt.psd(x, NFFT = 2048)
plt.psd(y, NFFT = 2048)
plt.psd(d, NFFT = 2048)
plt.grid(True)
plt.show()
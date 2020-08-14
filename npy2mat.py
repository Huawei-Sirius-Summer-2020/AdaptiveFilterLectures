# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:22:29 2020

@author: B00741681
"""

import numpy as np
#import scipy.signal as signal
#import matplotlib.pyplot as plt
import scipy.io as sio


x = np.load('data/gsm_4c_in.npy')
sio.savemat('data/gsm_4c_in.mat',  {'x':x})

y = np.load('data/gsm_4c_out.npy')
sio.savemat('data/gsm_4c_out.mat', {'y':y})




x = np.load('data/linear_lte_2c_data0_in.npy')
sio.savemat('data/linear_lte_2c_data0_in.mat',  {'x':x})

y = np.load('data/linear_lte_2c_data0_out.npy')
sio.savemat('data/linear_lte_2c_data0_out.mat', {'y':y})





x = np.load('data/linear_lte_2c_data1_in.npy')
sio.savemat('data/linear_lte_2c_data1_in.mat',  {'x':x})

y = np.load('data/linear_lte_2c_data1_out.npy')
sio.savemat('data/linear_lte_2c_data1_out.mat', {'y':y})




x = np.load('data/lte_2c_data0_in.npy')
sio.savemat('data/lte_2c_data0_in.mat',  {'x':x})

y = np.load('data/lte_2c_data0_out.npy')
sio.savemat('data/lte_2c_data0_out.mat', {'y':y})



x = np.load('data/lte_2c_data1_in.npy')
sio.savemat('data/lte_2c_data1_in.mat',  {'x':x})

y = np.load('data/lte_2c_data1_out.npy')
sio.savemat('data/lte_2c_data1_out.mat', {'y':y})



x = np.load('data/lte_4c_data0_in.npy')
sio.savemat('data/lte_4c_data0_in.mat',  {'x':x})

y = np.load('data/lte_4c_data0_out.npy')
sio.savemat('data/lte_4c_data0_out.mat', {'y':y})




x = np.load('data/lte_10c_data0_in.npy')
sio.savemat('data/lte_10c_data0_in.mat',  {'x':x})

y = np.load('data/lte_10c_data0_out.npy')
sio.savemat('data/lte_10c_data0_out.mat', {'y':y})




# -*- coding: utf-8 -*-
import numpy as np
from statistics import stdev 

N = 1000
K = 20000
mu0 = 2.0
D0  = 3.0

x = np.random.randn(K, N) * np.sqrt(D0) + mu0

E = np.zeros(K)
Var0 = np.zeros(K)
Var1 = np.zeros(K)
Var2 = np.zeros(K)
Var3 = np.zeros(K)


for k in range(K):
    y = x[k]
    # несмещенная состоятельная оценка мат. ожидания
    E[k]    = np.sum(y)/N
    
    # несмещенные состоятельные оценки дисперсии
    Var0[k]  = np.sum((y - E[k])**2) / (N-1)  # при оценки    мат. ожидания  
    Var1[k]  = np.sum((y - mu0)**2)  / N      # при известном мат. ожидании   
    
    # смещенные состоятельные оценки дисперсии
    Var2[k]  = np.sum((y - E[k])**2) / N     # при оценки    мат. ожидания
    Var3[k]  = np.sum((y - mu0)**2)  / (N-1) # при известном мат. ожидании   
    
    
print('E[E]    = %7.4f (d = %+7.5f)' %  (np.mean(E), np.mean(E) - mu0))
print('E[Var0] = %7.4f (d = %+7.5f)' %  (np.mean(Var0), np.mean(Var0) - D0))
print('E[Var1] = %7.4f (d = %+7.5f)' %  (np.mean(Var1), np.mean(Var1) - D0))
print('E[Var2] = %7.4f (d = %+7.5f)' %  (np.mean(Var2), np.mean(Var2) - D0))
print('E[Var3] = %7.4f (d = %+7.5f)\n\n' %  (np.mean(Var3), np.mean(Var3) - D0))

print('Var[E]    = %7.4f' %  stdev(E)**2)
print('Var[Var0] = %7.4f' %  stdev(Var0)**2)
print('Var[Var1] = %7.4f' %  stdev(Var1)**2)
print('Var[Var2] = %7.4f' %  stdev(Var2)**2)
print('Var[Var3] = %7.4f' %  stdev(Var3)**2)
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

#порядок фильтра
firord = 36

# вектор коэффициентов фильтра
w = signal.firwin(firord+1, 0.01)

# частота от -pi до pi
frq = np.linspace(-np.pi, np.pi, num = 2048, endpoint = False)

#расчет комплексного коэффициента передачи H(e^jw)
frq, h = signal.freqz(w, 1, worN = frq)

# АЧХ в дБ
# H = 10 log10(|H(e^jw)|^2) = 20 log10(|H(e^jw)|)
absh = 20*np.log10(abs(h))

#ФЧХ Ф(w) = arctan(Im[H(e^jw)] / Re[H(e^jw)] )
phi = np.arctan2(np.imag(h), np.real(h))

# график импульсной характеристики
plt.figure()
plt.stem(w)
plt.show()

#График АЧХ в дБ
plt.figure()
plt.plot(frq / np.pi, absh)
plt.show()

#График ФЧХ после раскрытия неоднозначности по фазе
plt.figure()
plt.plot(frq, np.unwrap(phi))
plt.show()


#фильтрация сигнала на фоне шума
N = 16384

#время
t = np.arange(0,N)

# исходный сигнал
x = np.sin(2*np.pi*0.01*t)

#сигнал + шум
xn = x + np.random.randn(N) * 0.3

# фильтрация КИХ фильтром
y = signal.lfilter(w, 1, xn)

# фильтрация через свертку
z = np.convolve(w,x, mode = 'full')

# график фильтрации во временной области
plt.figure()
plt.plot(t, xn, t, y, t, z[0:N], t, x,)


# результат фильтрации в частотной области
plt.figure()
plt.psd(x, 2048)
plt.psd(xn, 2048)
plt.psd(y, 2048)


# пояснение логарифмической шкалы дБ
x0 = np.sin(2*np.pi*0.01*t)
x1 = np.sin(2*np.pi*0.2*t)

y0 = signal.lfilter(w, 1, x0)
y1 = signal.lfilter(w, 1, x1)

# подавление x0 и x1 при прохождении через фильтр
D0 = 10*np.log10(sum(x0**2) / sum(y0**2))
print('x0 suppression %f dB' % D0)

D1 = 10*np.log10(sum(x1**2) / sum(y1**2))
print('x1 suppression %f dB' % D1)

# график спектральной плотности мощности
plt.figure()
plt.psd(x0, 2048)
plt.psd(x1, 2048)
plt.psd(y0, 2048)
plt.psd(y1, 2048)






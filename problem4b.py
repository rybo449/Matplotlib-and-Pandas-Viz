import matplotlib.pyplot as plt
import csv
from math import log
import sys
import datetime
import numpy as np
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

f = open(sys.argv[1])
reader = csv.reader(f)
next(reader)
tot = []
for i in xrange(4):
	tot.append([])
for i in reader:
	tot[0].append(float(i[0]))
	tot[1].append(float(i[1]))
	tot[2].append(float(i[2]))
	tot[3].append(float(i[3]))

f, axarr = plt.subplots(3, sharex = True)
alpha = ['A','B','C','D']
for i in xrange(1,4):
	if i == 2: 
		model = sm.OLS(tot[0], tot[i])
		results = model.fit()
		prstd, iv_l, iv_u = wls_prediction_std(results)
		axarr[i-1].plot(tot[i], tot[0], '.b')
		axarr[i-1].plot(tot[i], results.fittedvalues, 'r', label="OLS")
		axarr[i-1].set_title('Linear Best Fit for the best one')
		#axarr[i].set_ylabel('%c'%(alpha[i]))
		#axarr[i].set_xlabel('%c'%alpha[j])
	elif i == 3:
		z = np.polyfit(tot[0], tot[i], 3)
		f = np.poly1d(z)
		#model = sm.OLS(tot[i], tot[j])
		#results = model.fit()
		x_new = np.linspace(min(tot[0]), max(tot[0]), 100)
		y_new = f(x_new)
		axarr[i-1].set_title('Cubic Best Fit for the next best one')
		#prstd, iv_l, iv_u = wls_prediction_std(results)
		axarr[i-1].plot(tot[0], tot[i], 'o',x_new,y_new)
	elif i == 1:
		z = np.polyfit(tot[0], tot[i], 5)
		f = np.poly1d(z)
		#model = sm.OLS(tot[i], tot[j])
		#results = model.fit()
		x_new = np.linspace(min(tot[0]), max(tot[0]), 100)
		y_new = f(x_new)
		axarr[i-1].set_title('Degree-5 Best Fit for the worst one')
		#prstd, iv_l, iv_u = wls_prediction_std(results)
		axarr[i-1].plot(tot[0], tot[i], 'o',x_new,y_new)

plt.show()

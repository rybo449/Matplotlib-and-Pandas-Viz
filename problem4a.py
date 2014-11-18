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

f, axarr = plt.subplots(4,4, sharex = True, sharey = True)
alpha = ['A','B','C','D']
axarr[0][2].set_title('Correlation of Genes in the form of a Scatter Matrix', horizontalalignment='right')# horizontalalignment='center', verticalalignment='top')
for i in xrange(4):
	for j in xrange(4):
		model = sm.OLS(tot[i], tot[j])
		results = model.fit()
		prstd, iv_l, iv_u = wls_prediction_std(results)
		axarr[i][j].plot(tot[j], tot[i], '.b')
		axarr[i][j].set_ylabel('%c'%(alpha[i]))
		axarr[i][j].set_xlabel('%c'%alpha[j])

plt.show()

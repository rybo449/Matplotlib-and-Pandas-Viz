import matplotlib.pyplot as plt
import csv
from math import log
import sys
import datetime

f = open(sys.argv[1])
reader = csv.reader(f)
next(reader)
year = []
t = []
p = []
for i in reader:
	year.append(datetime.datetime.strptime(i[1],'%Y'))
	t.append(log(float(i[2]),10))
	p.append(i[0])

temp = [i for i in xrange(len(p))]
year1 = sorted(year)
p1 = [p[year.index(i)] for i in year1]
y1 = [year[year.index(i)] for i in year1]
t1 = [t[year.index(i)] for i in year1]

f, axarr = plt.subplots(2, sharex=True)
plt.title('# Transistors')
plt.setp(axarr, xticks = temp, xticklabels = p1)
plt.tick_params(axis = 'x', labelsize = 6)
axarr[0].plot(temp, t1, '.b--')
axarr[0].set_ylabel('Number of transistors in log10 scale')
axarr[0].set_title('# Transistors')
#axarr[0].set_xticklabels(axarr[0].xaxis.get_ticklabels(),rotation = 90)

axarr[1].set_title('Year of Introduction')
axarr[1].plot(temp, y1,'.r--')
axarr[1].set_ylabel('Year')
#axarr[1].set_xticklabels(axarr[1].xaxis.get_ticklabels(),rotation = 90)
plt.xlabel('Processor Name')
plt.show()

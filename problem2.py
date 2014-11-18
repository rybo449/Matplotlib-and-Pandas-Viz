import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from pandas import DataFrame
from _collections import defaultdict
import sys
import csv


f = open(sys.argv[1])
reader = csv.reader(f)
next(reader)

temp = []
for i in reader:
    temp.append(datetime.strptime(i[0],'%Y-%m-%d %H:%M:%S'))
timeDict=defaultdict(int)

for i in temp:
    timeDict[i.strftime('%m-%d')] += 1

tHours=pd.DataFrame.from_dict(timeDict, orient='index')
tHours.columns = ['timestamp']
ax = tHours['timestamp'].sort_index().plot(kind = 'bar', width = 1)

plt.xlabel('Date')
plt.ylabel('Frequency of the Timestamps')
plt.text(35,14400, "Histogram of Timestamps with Due Dates", horizontalalignment = 'center', fontsize=10)
plt.xticks(fontsize=10)
ax.vlines( 8, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 1')
plt.text(8,14005, "A0 & A1", fontsize=7)
ax.vlines( 23, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 2')
plt.text(23,14005, "A2", fontsize=7)
ax.vlines( 34, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 3')
plt.text(34,14005, "A3", fontsize=7)
ax.vlines( 52, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 4')
plt.text(52,14005, "A4", fontsize=7)
ax.vlines( 66, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 5')
plt.text(66,14005, "A5", fontsize=7)
ax.vlines( 62, 0,14000, linestyles = 'solid', color='r', label = 'Assignment 6')
plt.text(62,14005, "A6", fontsize=7)
plt.show()




import sys
import csv
import operator
import matplotlib.pyplot as plt
import datetime

f = open(sys.argv[1])
reader = csv.reader(f,delimiter = ',')
microsoft = []
date_stock = []
apple = []
next(reader)
for i in reader:
	microsoft.append(float(i[2]))
	apple.append(float(i[1]))
	date_stock.append(datetime.datetime.strptime(i[0],'%Y-%m'))
y = [apple[date_stock.index(min(date_stock))] for i in xrange(len(apple))]
y1 = [microsoft[date_stock.index(min(date_stock))] for i in xrange(len(microsoft))]


f, axarr = plt.subplots(2, sharex=True)

axarr[0].plot(date_stock, apple, '.b-')
axarr[0].plot(date_stock,y,'k--')
axarr[0].set_ylabel('Stock Price')
axarr[0].set_title('Apple Stock Prices from Jan-2006 to Sep-2008')
axarr[1].plot(date_stock, microsoft,'.r-')
axarr[1].plot(date_stock,y1,'k--')
axarr[1].set_title('Microsoft Stock Prices from Jan-2006 to Sep-2008')
axarr[1].set_ylabel('Stock Price')
plt.xlabel('Date')
plt.show()
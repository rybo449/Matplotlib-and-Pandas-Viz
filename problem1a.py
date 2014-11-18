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
L = []
for i in xrange(len(date_stock)-1,-1,-1):
	L.append(i)
y = [apple[date_stock.index(min(date_stock))] for i in xrange(len(apple))]

plt.plot(date_stock,apple,'.b-')
plt.plot(date_stock,y,'k--')
plt.title('Apple stock prices from Jan-2006 to Sep-2008')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.show()
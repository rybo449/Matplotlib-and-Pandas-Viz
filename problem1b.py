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

plt.plot(date_stock,apple,'.b-',label = 'Apple')
plt.plot(date_stock,microsoft,'.r-', label = 'Microsoft')
plt.plot(date_stock,y, 'k--')
plt.plot(date_stock,y1,'k--')
plt.title('Apple and Microsoft stock prices from Jan-2006 to Sep-2008')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend(loc = 2)
plt.show()
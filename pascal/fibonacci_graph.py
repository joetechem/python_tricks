import matplotlib.pyplot as fibo
import math

x = range(14)

y = [0, 1]

for i in range(12):
	y.append(y[i] + y[i+1])
	
print y

fibo.plot(x, y)
fibo.show()

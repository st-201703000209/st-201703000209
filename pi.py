from random import *
from math import *
times=100000 
count=0
for i in range(times):
	x=uniform(-1,1)
	y=uniform(-1,1)
	if x*x+y*y<=1:
		count=count+1
pi=count*4.0/times
print(pi)
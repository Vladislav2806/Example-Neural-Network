from random import randint
import numpy as np

def sigmoid(x):
	return 1/(1+np.exp(-x))

def func(x):
	return x*(1-x)

zadacha = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], \
			[1, 0, 1], [1, 1, 0], [1, 1, 1]]
answer = [0, 1, 0, 1, 0, 1, 0, 0]
sw = []	
L = 0.1

for i in [3, 3, 2]:
	sw.append([])
	for j in range(i):
		sw[-1].append(np.random.random())

for k in range(1000):
	yr = []
	for x, y in zip(zadacha, answer):
		f11 = sigmoid(sw[0][0]*x[0]+sw[0][1]*x[1]+sw[0][2]*x[2])
		f12 = sigmoid(sw[1][0]*x[0]+sw[1][1]*x[1]+sw[1][2]*x[2])

		f21 = sigmoid(sw[2][0]*f11+sw[2][1]*f12)
		if f21<0.5:
			yr.append(0)
		else:
			yr.append(1)

		e = (-1000*L)*(y-f21)
		d = e*f21*(1-f21)

		sw[2][0] -= L*d*f11
		sw[2][1] -= L*d*f12

		d11 = d*sw[2][0]*func(f11)
		d12 = d*sw[2][1]*func(f12)

		sw[1][0] -= d12*L*x[0]
		sw[1][1] -= d12*L*x[1]
		sw[1][2] -= d12*L*x[2]

		sw[0][0] -= d11*L*x[0]
		sw[0][1] -= d11*L*x[1]
		sw[0][2] -= d11*L*x[2]

	print(yr)
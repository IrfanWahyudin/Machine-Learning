w = [0.1,0.2]
print(w)

x = [[5, 3.2, 0.1], [4, 2.7 , 0.2]]
print(x)

t = [[], []]

y = [0.0 for yl in range(0,len(w))]

for i in range(0, len(x) - 1):	
	for j in range(0, len(w) - 1):
		y[j] = x[i] * w[j]
		print(y[j])


m = 0.2
w = [0.1,0.2]
print(w)

x = [5, 3.2, 0.1]
print(x)

t = [1.0, 0.0]

y = [0.0 for yl in range(0,len(w))]

error_tolerance = 0

for i in range(0, len(x) - 1):	
	for j in range(0, len(w) - 1):
		y[j] = x[i] * w[j]
		print(y[j])
		if t[j] <= y[j]:			
			print("update none")
		else:
			print("update weight")
			w[j] = w[j] + (m * (t[j] - y[j]) * x[i])
			error_tolerance


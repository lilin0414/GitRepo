l = []
for i in range(4):
	x = input("input a number:")
	l.append(x)
	l.sort()
for i in range(4):
	print(int(l[i]),end="  ")
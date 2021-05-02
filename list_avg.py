def avg(x):
	if (len(x)==0):
		return 0
	else:
		sum = 0
		for i in x:
			sum+=i
		return sum/len(x)

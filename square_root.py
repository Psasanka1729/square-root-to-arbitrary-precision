import math
def sqr(N,dec):
	digits = ''
	int_part = math.floor(math.sqrt(N))
	digits = digits + str(int_part) + '.'
	N = N - int_part * int_part
	N_str = str(N)+'00'
	N = int(N_str)
	s = int_part + int_part
	for n in range(dec):
		i = 1
		while True:
			if int(str(s)+str(i)) * i > N :
				div = int(str(s) + str(i-1))
				break
			else:
				i = i + 1
		digits = digits + str(i-1)
		N = N - div * (i-1)
		N_str = str(N) + '00'
		N = int(N_str)
		s = div + (i-1)
	return digits
print(sqr(3,20))

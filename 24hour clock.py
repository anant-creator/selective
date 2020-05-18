import time
h = 0
m = 0
s = 0
i = 0
j = 2
D = 30
M = 12
Y = 0
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
print("h","m","s","D","M","Y")
print("o","i","e","A","O","E")
print("u","n","c","Y","N","A")
print("r","t","d","S","T","R")
print("______")
while i < j:
	time.sleep(0)
	print(h, m, s, D, M, Y)
	j += 1
	i += 1
	s += 1
	ii = 4
	Y = 2020	
	if s == 60:
		m += 1
		s = 0
		if m == 60:
			h += 1
			m = 0
			if h == 24:
				h = 0
				D += 1
				if D == month_days[ii]:
					m += 1
					D = 0
					ii += 1
					if ii == 12:
						ii = 0
						if M == 12:
							Y += 1


				

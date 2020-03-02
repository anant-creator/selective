import time
h = 0
m = 0
s = 0
i = 0
j = 2
d = 0
m = 0
y = 0
print("h","m","s")
print("o","i","e")
print("u","n","c")
print("r","t","d")
print("______")
while i < j:
	time.sleep(1)
	print(h, m, s)
	j += 1
	i += 1
	s += 1
	if s == 60:
		m += 1
		s = 0
		if m == 60:
			h += 1
			m = 0
			if h == 24:
				h = 0
				
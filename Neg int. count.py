given_list = [10, 20, -50, -70, -80, -20, -30]

total = 0
k = len(given_list) - 1
while given_list[k] < 0:
	total += given_list[k]
	k -= 1
print(total)
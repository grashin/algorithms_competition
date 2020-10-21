expression = list(input())
len_1 = len(expression)
counter = 0
for i in range(len(expression)):
	letter = expression[i]
	if ord(letter) == 32:
		continue
	if ord(letter)<91 and ord(letter)>64:
		counter += 1
	else:
		if counter > 4 :
			len_1 += 4
		else:
			len_1 += counter
		counter = 0
if counter > 2:
	len_1 += 2
else:
	len_1 += counter
print(len_1)
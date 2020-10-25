# expression = list(input())
# len_1 = len(expression)
# counter = 0
# for i in range(len(expression)):
# 	letter = expression[i]
# 	if ord(letter) == 32:
# 		continue
# 	if ord(letter)<91 and ord(letter)>64:
# 		counter += 1
# 	else:
# 		if counter > 4 :
# 			len_1 += 4
# 		else:
# 			len_1 += counter
# 		counter = 0
# if counter > 2:
# 	len_1 += 2
# else:
# 	len_1 += counter
# print(len_1)

# hhh HHH h HHH
# hhhHHHhHHH
# 0001110111
# Hello World
# AAAAaAAAAbbbbbbb   5 vs 8

expression = list(input())
len_1 = len(expression)
print(len_1)
counter = 0
shift = False
to_delete_from_shift = 0
to_delete_from_not_shift = 0
for i in range(len(expression)):
	letter = expression[i]
	if ord(letter) == 32:
		continue

	if ord(letter)<91 and ord(letter)>64:
		if shift:
			counter -= 1 
			to_delete_from_shift += 1
		else:
			counter += 1
			to_delete_from_not_shift += 1
	elif ord(letter)>90:
		if shift:
			counter += 1
			to_delete_from_not_shift += 1
		else:
			counter -= 1
			to_delete_from_shift += 1

	if counter > 4 :
		len_1 += 2# + to_delete_from_shift
		shift = not shift
		counter = 0
		to_delete_from_shift = 0
	elif counter < -2:
		# len_1 += to_delete_from_not_shift
		counter = 0
		to_delete_from_not_shift = 0

if counter > 2:
	len_1 += 2 #+ to_delete_from_shift
else:
	len_1 += to_delete_from_not_shift
print(len_1)

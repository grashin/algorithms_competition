lucky_numbers = input()
lucky_numbers = lucky_numbers.split()
# print(lucky_numbers)
n = input()
for i in range(int(n)):
	user_numbers = input()
	user_numbers = user_numbers.split()
	# print(user_numbers)
	counter = 0
	for j in range(6):
		if user_numbers[j] in lucky_numbers:
			# print(user_numbers[j])
			counter+=1
	if counter>=3:
		print('Lucky')
	else:
		print('Unlucky')


# условия https://yandex.ru/cup/algorithm/analysis/
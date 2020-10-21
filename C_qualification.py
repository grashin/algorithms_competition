import numpy as np

number_of_tests = int(input())



def check_addition(arr_1, arr_2, multiplier):
	addition = arr_2[0]-arr_1[0]*multiplier
	print('addition', addition, 'multiplier', multiplier)
	for i in range(1, len(arr_1)):
		if not (addition == arr_2[i]-arr_1[i]*multiplier):
			return False
	return True

# def get_composites(arr_1):


result = []
for i in range(number_of_tests):
	len_1 = int(input())
	arr_1 = input()
	arr_1 = np.sort(np.array(arr_1.split(), np.uint8))
	len_2 = int(input())
	arr_2 = input()
	arr_2 = np.sort(np.array(arr_2.split(), np.uint8))

	if len_1 == len_2 and len_1<2:
		result.append('YES')
		continue
	elif len_1 != len_2:
		result.append('NO')
		continue
	ok = False
	max_multiplier = int(arr_2[-1]/arr_1[-1])
	print('max_mult', max_multiplier)
	for multiplier in range(1, max_multiplier+1):
		ok = check_addition(arr_1, arr_2, multiplier)
		if ok:
			result.append('YES')
			break
	if not ok:
		result.append('NO')
print(result)


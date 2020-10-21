string = input()
ending = True
# string = string.split()
index = 1
def check_palindrom(string):
	i=0
	n = len(string)
	while True:
		# print(i, n-i)
		if string[i] == string[n-1-i]:
			i+=1
			if i == int(len(string)/2):
				return True, string
		else:
			return False, None
while ending:
	index+=1
	for j in range(len(string)-index+1):	
		# print(string[j:j+index])
		res, answer = check_palindrom(string[j:j+index])
		if res:
			print(answer)
			ending = False
			break
	if index == len(string)-1 and ending: 
		print('-1')
		ending = False
	
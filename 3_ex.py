 # number_of_figures = int(input())
# def eqaution_btw_figures(p1, p2):
# 	return p1[2]*(p1[1]-p2[1])-p1[1]*(p1[2]-p2[2]), (p1[2]-p2[2])/(p1[1]-p2[1])
# def get_center(p):
# 	return (p[0]+p[2]+p[4]+p[6])/4, (p[1]+p[3]+p[5]+p[7])/4
# def right(b, k, center_x, center_y):
# 	if abs(center_y-center_x*k-b) < 0.01:
# 		return True
# 	else:
# 		return False
# def identical(p1, p2):
# 	if p1[1] == p2[1] and p1[2] == p2[2]:
# 		return True
# 	else:
# 		return False
# k, b = 0, 0
# array_values = []
# ok = True
# center_x_1, center_y_1 = 0, 0
# k_ref, b_ref = 0, 0
# identical_value = False
# for i in range(number_of_figures):
# 	values = input()
# 	values = values.split()
# 	values = [int(i) for i in values]
# 	if values[0] == 0:
# 		# array_values.append(values)
# 		center_x, center_y = values[1], values[2]
# 	else:
# 		center_x, center_y = get_center(values[1:])
# 	if i == 0:
# 		center_x_1, center_y_1 = center_x, center_y
# 	elif i == 1 or identical_value:
# 		if identical([0, center_x, center_y],  [0, center_x_1, center_y_1]):
# 			identical_value = True
# 		else:
# 			identical_value = False
# 			b_ref, k_ref = eqaution_btw_figures([0, center_x, center_y],  [0, center_x_1, center_y_1])
# 	else:
# 		ok = right(b_ref, k_ref, center_x, center_y)
# 		if not ok:
# 			break
# if ok or number_of_figures < 3:
# 	print('Yes')
# else:
# 	print('No')

number_of_figures = int(input())

def eqaution_btw_figures(p1, p2):
	return p1[2]*(p1[1]-p2[1])-p1[1]*(p1[2]-p2[2]), (p1[2]-p2[2])/(p1[1]-p2[1])
def PreIsPointsOnLine(x1, y1, x2, y2):
	dx = x2 - x1	
	dy = y2 - y1
	ds = x1 * y2 - x2 * y1
	return dx, dx, ds

def IsPointsOnLine(dx, dy, ds, x3, y3):
  return (x3 * dy - y3 * dx == ds)

		
def get_center(p):
	return (p[0]+p[2]+p[4]+p[6])/4, (p[1]+p[3]+p[5]+p[7])/4
def right(x_1, y_1, x_2, y_2, x_3, y_3):
	if x2 - x1 == 0 or x3-x1 == 0 or x3-x2 == 0 or ((x_3 - x_1) / (x_2 - x_1) == (y_3 - y_1) / (y_2 - y_1)):
		return True
	else:
		return False

def identical(p1, p2):
	if p1[1] == p2[1] and p1[2] == p2[2]:
		return True
	else:
		return False
k, b = 0, 0
array_values = []
ok = True

center_x_1, center_y_1, center_x_2, center_y_2 = 0, 0, 0, 0
k_ref, b_ref = 0, 0
identical_value = False
dx, dy, ds = 0, 0, 0
for i in range(number_of_figures):
	values = input()
	values = values.split()
	values = [int(i) for i in values]
	if values[0] == 0:
		# array_values.append(values)
		center_x, center_y = values[2], values[3]
		print(center_x, center_y)
	else:
		center_x, center_y = get_center(values[1:])
	if i == 0:
		center_x_1, center_y_1 = center_x, center_y
	elif i == 1 or identical_value:
		if identical([0, center_x, center_y],  [0, center_x_1, center_y_1]):
			identical_value = True
		else:
			identical_value = False
			dx, dy, ds = PreIsPointsOnLine(center_x_1, center_y_1, center_x, center_y)
	else:
		ok = IsPointsOnLine(dx, dy, ds, center_x, center_y)
		print(ok, center_x, center_y, dx, dy ,ds)
		if not ok:
			break
if ok or number_of_figures < 3:
	print('Yes')
else:
	print('No')
	

	
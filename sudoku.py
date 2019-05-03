import os
import cv2
import random


frame = cv2.imread("./frame.jpg")
frame = cv2.resize(frame, (360, 360))

cell  = [[0 for i in range(9)] for j in range(9)]


def first_parts(position):
	cnt = 0
	counted = []
	if position == 'center':
		start_y = 3
		start_x = 3
	elif position == 'upright':
		start_y = 0
		start_x = 0
	
	for i in range(3):
		for j in range(3):
			
			while True:
				break_check = 0
				num = random.randrange(9)+1
				for s in range(cnt):
					if num == counted[s]:
						break_check=1
				if break_check == 0:
					break
				
			counted.append(num)
			
			cell[start_x][start_y] = num
			start_y = start_y + 1
			if position == 'center':
				if start_y == 6:
					start_y = 3
					start_x = start_x + 1
			elif position == 'upright':
				if start_y == 3:
					start_y = 0
					start_x = start_x + 1
				
			cnt = cnt + 1
		
first_parts('upright')
first_parts('center')		
	
def second_parts(direction):
	
	if direction == 'horizontal':
		rotated_cell  = [[0 for i in range(9)] for j in range(9)]
		for i in range(9):
			for j in range(9):
				rotated_cell[i][j] = cell[j][i]
		
	
	for_cross = [[0 for i in range(9)] for j in range(3)]
	for num in range(1, 9+1, 1):
		
		for i in range(3):
			for j in range(3):
				if direction == 'horizontal' and rotated_cell[i+3][j+3] == num:
					column = i
				elif direction == 'vertical' and cell[i+3][j+3] == num:
					column = i
					
		for i in range(3):
			if i!=column:
				for_cross[i][num-1] = num
		
	one2six = [1,2,3,4,5,6]
	from_column = random.sample(one2six, 3)
	
	left = []
	for i in from_column:
		cnt = 0
		for num in range(1, 9+1, 1):
			if for_cross[0][num-1] == num:
				cnt = cnt + 1
				if cnt == i:
					left.append(num)
					for_cross[1][num-1] = 0
					for_cross[2][num-1] = 0
				
				
	central_cnt = 0
	right_cnt = 0
	right = []
	center = []
	for i in range(9):
		if for_cross[1][i]!=0:
			central_cnt = central_cnt + 1	
		if for_cross[2][i]!=0:
			right_cnt = right_cnt + 1
			
	def other2columns(column_num, column_cnt, column, other_col_num, other_column):
		one2xxx = []
		for i in range(column_cnt):
			one2xxx.append(i+1)
		from_column = random.sample(one2xxx, 3)
		
		for i in from_column:
			cnt = 0
			for num in range(1, 9+1, 1):
				if for_cross[column_num][num-1] == num:
					cnt = cnt + 1
					if cnt == i:
						column.append(num)
						for_cross[0][num-1] = 0
						for_cross[other_col_num][num-1] = 0
						
		for i in range(9):
			if for_cross[other_col_num][i]!=0:
				other_column.append(i+1)
			
			
	if central_cnt >= right_cnt:
		other2columns(2, right_cnt, right, 1, center)			
	else:
		other2columns(1, central_cnt, center, 2, right)
	
	if direction == 'vertical':			
		for i in range(3):
			cell[3][6+i] = left[i]
			cell[4][6+i] = center[i] #have problem? list index out of range. Problem should be in center and right
			cell[5][6+i] = right[i]  #have problem?
	elif direction == 'horizontal':
		for i in range(3):
			cell[6+i][3] = left[i]
			cell[6+i][4] = center[i] #have problem?
			cell[6+i][5] = right[i]  #have problem?


second_parts('horizontal')
second_parts('vertical')



## for bottom right corner
corner_cell  = [[0 for i in range(0)] for j in range(9)]

for num in range(1, 9+1, 1):
	
	for i in range(3):
		for j in range(3):
			if cell[6+i][3+j] == num: #center right
				col1 = i
				#row1 = 3+j
			if cell[3+i][6+j] == num: #bottom center
				#col2 = 3+i
				row2 = j
				
	for i in range(9):
		if i != col1 and i != col1+3 and i != col1+6: #for x-cordinate
			if i != row2*3 and i != row2*3+1 and i != row2*3+2: #for y-cordinate
				corner_cell[i].append(num)
		
for i in range(9):
	min_len = 9	
	for j in range(9):
		if min_len > len(corner_cell[j]):
			min_len = len(corner_cell[j])
			min_id = j
	
	corner_x = min_id%3
	corner_y = min_id/3
	
	target = corner_cell[min_id][0]
	cell[6+corner_x][6+corner_y] = target
	
	for j in range(9):
		if target in corner_cell[j]:
			corner_cell[j].remove(target)
			
	corner_cell[min_id] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	


for_two_cells  = [[0 for i in range(0)] for j in range(6)]

	
for i in range(6):
	
	for num in range(1, 1+9, 1):
		for j in range(6):
			if cell[3+i][3+j] == num:
				break
		else:
			for_two_cells[i].append(num)

print(for_two_cells[0])
print(for_two_cells[1])
print(for_two_cells[2])
print(for_two_cells[3])
print(for_two_cells[4])
print(for_two_cells[5])






	
#show image
for i in range(13, 364, 39):
	for j in range(33, 384, 39):
		frame = cv2.putText(frame, str(cell[(i-13)/39][(j-33)/39]), (i,j), cv2.FONT_HERSHEY_SIMPLEX,  1, (0,0,0), 2)	

cv2.imshow('sudoku', frame)
cv2.waitKey(0)

import os
import cv2
import random


frame = cv2.imread("./frame.jpg")
frame = cv2.resize(frame, (360, 360))

cnt = 0
counted = []
cell  = [[0 for i in range(9)] for j in range(9)]
central_y = 3
central_x = 3

#for central 9 cells
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
		
		cell[central_x][central_y] = num
		central_y = central_y + 1
		if central_y == 6:
			central_y = 3
			central_x = central_x + 1
		cnt = cnt + 1
		
		
	
def second_parts():
	for_cross = [[0 for i in range(9)] for j in range(3)]
	for num in range(1, 9+1, 1):
		
		for i in range(3):
			for j in range(3):
				if cell[i+3][j+3] == num:
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
	
				
	for i in range(3):
		cell[3][6+i] = left[i]
		cell[4][6+i] = center[i]
		cell[5][6+i] = right[i]
		
	print('')
	for i in range(9):
		print(for_cross[0][i], for_cross[1][i], for_cross[2][i])
		



second_parts()
	
#show image
for i in range(13, 364, 39):
	for j in range(33, 384, 39):
		frame = cv2.putText(frame, str(cell[(i-13)/39][(j-33)/39]), (i,j), cv2.FONT_HERSHEY_SIMPLEX,  1, (0,0,0), 2)	

cv2.imshow('sudoku', frame)
cv2.waitKey(0)

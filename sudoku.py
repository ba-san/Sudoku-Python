import os
import cv2
import random


frame = cv2.imread("./frame.jpg")
frame = cv2.resize(frame, (360, 360))
frame = cv2.putText(frame,'0', (10,32), cv2.FONT_HERSHEY_SIMPLEX,  1, (0,0,0), 2)

cnt = 0
counted = []
cell  = [[0]*9]*9
central_y = 3
central_x = 3

#for central 9 cells
for i in range(130, 231, 39):
	for j in range(150, 251, 39):
		
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
		print(central_x, central_y, cell[central_x][central_y])
		central_y = central_y + 1
		if central_y == 6:
			central_y = 3
			central_x = central_x + 1
		cnt = cnt + 1
		frame = cv2.putText(frame, str(num), (i,j), cv2.FONT_HERSHEY_SIMPLEX,  1, (0,0,0), 2)
	
#for i in range(3):
#	for j in range(3):
#		#print(central_x+i-3, central_y+j)
#		print("{} ".format(cell[central_x+i-3][central_y+j]))
#	print('')

for i in range(9):
	for j in range(9):
		#print(central_x+i-3, central_y+j)
		print("{} ".format(cell[i][j]))
	print('')
	
print(cell[3][3])
print(cell[3][4])
print(cell[3][5])
print(cell[4][3])
print(cell[4][4])
print(cell[4][5])
print(cell[5][3])
print(cell[5][4])
print(cell[5][5])

cv2.imshow('sudoku', frame)
cv2.waitKey(0)

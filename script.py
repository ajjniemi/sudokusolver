sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0]]

import numpy as np 
def printsudo():
	global sudoku
	for y in range(9):
		print("{} {} {} | {} {} {} | {} {} {}" .format(sudoku[y][0],sudoku[y][1],sudoku[y][2],sudoku[y][3],sudoku[y][4],sudoku[y][5],sudoku[y][6],sudoku[y][7],sudoku[y][8]))
		if(y==2 or y==5):
			print("------+-------+------")

def insert():
	global sudoku
	for y in range(9):
		for x in range(9):
			print("")
			sudoku[y][x] = "X"
			printsudo()
			sudoku[y][x] = int(input("Give number to X:") or "0")
	
def possible(y, x, n):
	global sudoku
	for i in range(9):
		if sudoku[y][i] == n:
			return False
	for i in range(9):
		if sudoku[i][x] == n:
			return False
	yy = (y//3)*3
	xx = (x//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if sudoku[yy+i][xx+j] == n:
				return False
	return True

def solve():
	global sudoku
	for y in range(9):
		for x in range(9):
			if(sudoku[y][x] == 0):
				for n in range(1,10):
					if possible(y, x, n):
						sudoku[y][x] = n
						solve()
						sudoku[y][x] = 0
				return
	printsudo()
	input("next?")
insert()
solve()

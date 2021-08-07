import json
import requests
import pprint

def isPossible(x,y,n):
    for i in range(9):
        if sudoku[x][i] == n:
            return False
        if sudoku[i][y] == n:
            return False
    x_square = (x//3)*3
    y_square = (y//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[x_square + i][y_square + j] == n:
                return False
    return True

def solveSudoku():
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                for n in range(1,10):
                    if isPossible(x,y,n):
                        sudoku[x][y] = n
                        solveSudoku()
                        sudoku[x][y] = 0
                    return


diff = ["easy", "medium", "hard", "random"]
res = requests.get(f'https://sugoku.herokuapp.com/board?difficulty={diff[0]}')
sudoku = res.json()
sudoku = sudoku["board"]
pprint.pprint(sudoku)
solveSudoku()
pprint.pprint(sudoku)








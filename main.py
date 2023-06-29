import random
import numpy as np

def random_state(height, width):
    board_state=[]
    for i in range(height):
        row=[]
        for j in range (width):
            random_number=  random.random()
            if (random_number>=0.5):
                 cell_state=1
            else:
                 cell_state=0
            row.append(cell_state)
        board_state.append(row)
    return board_state

def calcNeighbours(board_state,i,j):
    rows=len(board_state)
    columns= len(board_state[0])
    sum=0
    if (i==0):
        if (j==0 or j==columns-1):
            for x in range (2):
                for y in range (2):
                    sum+=board_state[i+x][j+y]
    else:
        for x in range(-1,2):
            for y in range (-1,2):
                sum+=board_state[i+x][j+y]
        sum-=board_state[i][j]        # So that it doesn't count itself



def next_board_state(board,rows,columns):
    for i in range(rows):
        for j in range(columns):
            pass
            


def render(board_state):
    rows=len(board_state)
    columns= len(board_state[0])
    for i in range(rows):
        for j in range(columns):
            if board_state[i][j] == 1:
                print("#", end=" ")
            else:
                print(" ", end=" ")
            if j < columns - 1:
                print("|", end=" ")  # Add vertical grid lines
        print()
        if i < rows - 1:
            print("- " * columns)  # Add horizontal grid lines




random.seed(None,version=2)

a_random_state = random_state(20, 30)
render(a_random_state)


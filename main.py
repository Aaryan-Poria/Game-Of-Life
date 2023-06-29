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
    total_sum=0
    if (i==0 or i==rows-1):
        if (j==0):
            for x in range (2):
                for y in range (2):
                    print(f'board-state value: {board_state[i+x][j+x]}')
                    total_sum+=board_state[i+x][j+y]
        elif (j==columns-1):
            for x in range(2):
                for y in range(-1,1):
                    total_sum += board_state[i + x][j + y]
        else:
            if (i==0): # Top Row
                for x in range(2):
                    for y in range (-1,2):
                        total_sum += board_state[i + x][j + y]
            else:
                for x in range (-1,2):
                    for y in range (-1,1):
                        total_sum += board_state[i + x][j + y]
    elif (j==0):
        for x in range (2):
            for y in range (-1,2):
                total_sum += board_state[i + x][j + y]
    elif (j==columns-1):
        for x in range (-1,1):
            for y in range(-1,2):
                total_sum += board_state[i + x][j + y]
    else:
        for x in range(-1,2):
            for y in range (-1,2):
                total_sum+=board_state[i+x][j+y]
    total_sum-=board_state[i][j]        # So that it doesn't count itself
    return total_sum

    

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

lst=[[1,0,1,1],[1,1,0,1],[0,0,1,1],[1,1,1,0]]


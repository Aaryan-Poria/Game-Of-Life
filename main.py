import random
import numpy as np

def randomstate(board_state,height, width):
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


def printboard_state(board_state, rows, columns):
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
board_state=[]
height=5
width=5
randomstate(board_state,height,width)
printboard_state(board_state,height,width)



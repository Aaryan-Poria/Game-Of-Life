import random
import numpy as np

global rows
global columns

def dead_state():
    board_state=[]
    for i in range(rows):
        row=[]
        for j in range (columns):
           row.append(0)
        board_state.append(row)
    return board_state

def random_state():
    board_state=[]
    for i in range(rows):
        row=[]
        for j in range (columns):
            random_number=  random.random()
            if (random_number>=0.5):
                 cell_state=1
            else:
                 cell_state=0
            row.append(cell_state)
        board_state.append(row)
    return board_state

def calcNeighbours(board_state,i,j):
    total_sum=0
    if (i==0):
        if (j==0):
            for x in range (2):
                for y in range (2):
                    total_sum+=board_state[i+x][j+y]
        elif (j==columns-1):
            for x in range(0,2):
                for y in range(-1,1):
                    total_sum += board_state[i + x][j + y]
        else:
            if (i==0): # Top Row
                for x in range(0,2):
                    for y in range (-1,2):
                        total_sum += board_state[i + x][j + y]
            else:
                for x in range (-1,1):
                    for y in range (-1,):
                        total_sum += board_state[i + x][j + y]
    elif (i==rows-1):
        if (j==0):
            for x in range(-1,1):
                for y in range (2):
                    total_sum += board_state[i + x][j + y]
        elif (j==columns-1):
            for x in range (-1,1):
                for y in range (-1,1):
                    total_sum += board_state[i + x][j + y]
        else:
            for x in range(-1,1):
                for y in range(-1,2):
                    total_sum += board_state[i + x][j + y]

    elif (j==0):
        for x in range (-1,2):
            for y in range (0,2):
                total_sum += board_state[i + x][j + y]
    elif (j==columns-1):
        for x in range (-1,2):
            for y in range(-1,1):
                total_sum += board_state[i + x][j + y]
    else:
        for x in range(-1,2):
            for y in range (-1,2):
                total_sum+=board_state[i+x][j+y]
    total_sum-=board_state[i][j]        # So that it doesn't count itself
    return total_sum

    

def next_board_state(initial_state):
    new_state=dead_state()
    for i in range(rows):
        for j in range(columns):
            liveNeighbours=calcNeighbours(initial_state,i,j)
            if initial_state[i][j]==1 and (liveNeighbours==2 or liveNeighbours==3):
                new_state[i][j]=1
            elif (initial_state[i][j]==0 and liveNeighbours==3):
                new_state[i][j]=1
            else:
                new_state[i][j]=0
    return new_state

def render(board_state):
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

def unitTest(initial_state, next_state):
    expected_state = None
    if initial_state == [[0,0,0],
                         [0,0,0],
                         [0,0,0]]:
        print("In Condition-1")
        expected_state = [[0,0,0],
                          [0,0,0],
                          [0,0,0]]
    elif initial_state == [[0,0,1],
                           [0,1,1],
                           [0,0,0]]:
        print("In Condition 2")
        expected_state = [[0,1,1],
                          [0,1,1],
                          [0,0,0]]
    elif initial_state==[
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]]:
        print("In Condition-3")
        expected_state=[[0,0,0],
                        [1,1,1],
                        [0,0,0]
                        ]
    print(expected_state==next_state)




random.seed(None,version=2)

rows=4
columns=4
initial_state=[
  [1, 0, 0, 1],
  [0, 1, 1, 0],
  [0, 1, 1, 0],
  [1, 0, 0, 1]
]
nextState=next_board_state(initial_state)
render(nextState)


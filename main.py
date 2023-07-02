import random
import numpy as np
import os

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

def readFromFile():
    file1 = open("toad.txt", mode="r", encoding="utf-8")
    file1.seek(0)  
    lines = file1.readlines()
    file1.close()
    array_2d = [[int(char) for char in line.strip()] for line in lines]
    return array_2d

random.seed(None,version=2)

start_state= readFromFile()
rows= len(start_state)
columns= len(start_state[0])

render(start_state)
while True:
    input("Press Enter to generate the next state: ")
    new_state=next_board_state(start_state)
    if os.name=="nt":
        _=os.system("cls")
    else:
        _=os.system("clear")

    render(new_state)
    start_state=new_state






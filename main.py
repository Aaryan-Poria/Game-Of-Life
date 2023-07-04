import random
import os


def dead_state(rows, columns):
    board_state = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        board_state.append(row)
    return board_state


def random_state(rows, columns):
    board_state = []
    for i in range(rows):
        row = []
        for j in range(columns):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = 1
            else:
                cell_state = 0
            row.append(cell_state)
        board_state.append(row)
    return board_state


def expand_board(input_board, num_rows, num_cols):
    # Step 1: Determine the current dimensions of the input board
    curr_rows = len(input_board)
    curr_cols = len(input_board[0])

    # Step 2: Calculate the desired dimensions for the expanded board
    expanded_rows = curr_rows + 2 * num_rows
    expanded_cols = curr_cols + 2 * num_cols

    # Step 3: Create a new expanded board with the desired dimensions
    expanded_board = [[0] * expanded_cols for _ in range(expanded_rows)]

    # Step 4: Copy the contents of the input board into the expanded board
    for i in range(curr_rows):
        for j in range(curr_cols):
            expanded_board[i + num_rows][j + num_cols] = input_board[i][j]

    # Step 5: Return the expanded board
    return expanded_board


def calc_neighbours(board_state, i, j):
    alive_neighbours = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue  # Skip the current cell
            try:
                if i + x >= 0 and j + y >= 0:  # Check if indices are within bounds
                    alive_neighbours += board_state[i + x][j + y]
            except IndexError:
                continue
                # Ignore index errors (out of bounds)
                # They may still occur for edge cases
    return alive_neighbours


def next_board_state(initial_state, rows, columns):
    next_state = dead_state(rows, columns)
    for i in range(rows):
        for j in range(columns):
            alive_neighbours = calc_neighbours(initial_state, i, j)
            if initial_state[i][j] == 1 and (
                alive_neighbours == 2 or alive_neighbours == 3
            ):
                next_state[i][j] = 1
            elif initial_state[i][j] == 0 and alive_neighbours == 3:
                next_state[i][j] = 1
            else:
                next_state[i][j] = 0
    return next_state


def render(board_state, rows, columns):
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


def read_from_file():
    file1 = open("toad.txt", mode="r", encoding="utf-8")
    file1.seek(0)
    lines = file1.readlines()
    file1.close()
    array_2d = [[int(char) for char in line.strip()] for line in lines]
    return array_2d


random.seed(None, version=2)

start_state = read_from_file()
start_state = expand_board(start_state, 5, 5)

current_rows = len(start_state)
current_cols = len(start_state[0])

render(start_state, current_rows, current_cols)

while True:
    input("Press Enter to generate the next state: ")
    new_state = next_board_state(start_state, current_rows, current_cols)
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

    render(new_state, current_rows, current_cols)
    start_state = new_state

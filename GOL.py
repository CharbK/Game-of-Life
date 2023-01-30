import os
import random
import time

import colorama


def print_board(board):
    os.system("clear")
    print(colorama.Fore.YELLOW, end = "")
    height, width = len(board), len(board[0])
    line = "-"*(width*2+1)
    print(line)
    for i in range(height):
        row_to_print = "|"
        for j in range(width):
            row_to_print += "  " if board[i][j] == 0 else "* "
        row_to_print = row_to_print[0:(len(row_to_print)-1)]
        row_to_print += "|"
        print(row_to_print)
    print(line)

def generateBoard(width, height, prob):
    board = []
    for j in range(height):
        row = []
        for i in range(width):
            add = 0
            if random.randint(1,prob) == 1:
                add = 1
            row.append(add)
        board.append(row)
    return board

def gameOfLife(board):
    height, width = len(board), len(board[0])
    def check(i, j):
        if i < 0 or i >= height or j < 0 or j >= width:
            return 0
        if board[i][j] > 0:
            return 1
        return 0
    def count(i, j) -> None:
        amount = sum([check(y,x) for y,x in
                    [
                        (i-1,j-1),(i-1,j),(i,j-1),(i-1,j+1),
                        (i+1,j+1),(i+1,j),(i,j+1),(i+1,j-1),
                    ]
                    ])
        if board[i][j] > 0:
            board[i][j] = max(amount,1)
        else:
            board[i][j] = -amount
    def update(i, j):
        live_neighbors = abs(board[i][j])
        if board[i][j] > 0:
            if live_neighbors < 2 or live_neighbors > 3:
                board[i][j] = 0
            else:
                board[i][j] = 1
        else:
            if live_neighbors == 3:
                board[i][j] = 1
            else:
                board[i][j] = 0
    for i in range(height):
        for j in range(width):
            count(i,j)
    for i in range(height):
        for j in range(width):
            update(i,j)
    return board

if __name__ == "__main__":
    board = generateBoard(15,15,3)
    print_board(board)
    while 1:
        gameOfLife(board)
        print_board(board)
        time.sleep(0.5)

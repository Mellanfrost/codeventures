from tester import test


# 37. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver


"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],
]

Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"],
]

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""


def solution_one(board):
    def valid_move(board, row, col, value):
        if value in board[row]:
            return False
        for i in range(9):
            if board[i][col] == value:
                return False
        row_idx, col_idx = row - row%3, col - col%3
        for i in range(row_idx,row_idx+3):
            for j in range(col_idx,col_idx+3):
                if board[i][j] == value:
                    return False
        return True

    def solve(row, col):
        if row == 9:
            return True
        if col == 9:
            return solve(row+1, 0)
        if board[row][col] != ".":
            return solve(row, col+1)
        for val in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if valid_move(board, row, col, val):
                board[row][col] = val
                if solve(row, col):
                    return True
                board[row][col] = "."
        return False
    
    solve(0, 0)


# TESTING
# --------------------

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],
]

output = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"],
]

test_cases = [
    [[board], output],
]

def solution_wrapper(func):
    def wrapper(board):
        func(board)
        return board
    return wrapper

test(solution_wrapper(solution_one), test_cases)

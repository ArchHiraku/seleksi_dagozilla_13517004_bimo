#!/usr/bin/env python

'''
SELEKSI CALON KRU PROGRAMMING DAGOZILLA 2018
Take Home Test
File name: sudoku.py
Problem 2: Code Comprehension
'''

import sys
import numpy as np

def read_from_file(filename, board):
    with open(filename) as f:
        data = f.readlines()

    for i in range(9):
        for j in range(9):
            if data[i][j] == '-':
                board[i][j] = int(0)
            else:
                board[i][j] = int(data[i][j])


# What does this function do?
# output the data in sudoku board
def print_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                print '-',
            else:
                print board[i][j],
        print('')
 

def save_board(filename, board):
    np.savetxt(filename, board, delimiter=' ', fmt='%i')


# What does this function do?
# if there is an empty location on the board, change the value of l with an empty location, then return True. Else return False
def find_empty_location(board, l):
    for row in range(9):
        for col in range(9):
            # What happens inside the 'if' section?
            # if the location on [row,col] is empty, writes it to l and return True
            if(board[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False
    # Why does this function return a boolean value?
    # to let us know if there exists empty location on the board


def used_in_row(board, row, num):
    for i in range(9):
        if(board[row][i] == num):
            return True
    return False


def used_in_col(board, col, num):
    for i in range(9):
        if(board[i][col] == num):
            return True
    return False


def used_in_block(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if(board[i+row][j+col] == num):
                return True
    return False


def is_valid(board, row, col, num):
    return not used_in_row(board, row, num) \
        and not used_in_col(board,col,num) \
        and not used_in_block(board,row - row%3,col - col%3,num)
    # What makes this function return True (what makes it valid for a number in a given location)?
    # if said number has not appeared on the same row, column, or block


# Explain the algorithm in this function!
# Using bruteforce, the function finds an empty location on the board, put a valid number on it, and calls the function again. If it fails, said number is changed until the board finds a valid solution (as in all empty squares have been given a valid number (the algorithm does not check if the problem board have the same number in some rows, columns, or blocks)), or all possible numbers has been tried and no valid solution has been found, where the function return False.
def solve_sudoku(board):
     
    # 'l' is a list that stores rows and cols in find_empty_location Function
    l=[0,0]
     
    # What does this 'if' block check?
    # run the find_empty_location function, halts the solve_sudoku function if the board is all filled up
    # What will happen if the program enters the following 'if' block?
    # the board is filled up and the solve_sudoku function will return True
    if(not find_empty_location(board, l)):
        # In what way does this True value affect the program?
        # the program will print and save the solution
        return True

    # Assigning list values to row and col that we got from the above Function 
    row=l[0]
    col=l[1]

    # What does this block do?
    # tries to give a valid number on an empty location and solves the resulting board recursively with calling the solve_sudoku function. If it fails, undo giving the number on said empty location
    for num in range(1,10):
        if is_valid(board, row, col, num):
            board[row][col]=num

            # What does this 'if' section check?
            # whether the board with the added number is solved
            if solve_sudoku(board):
                return True
 
            # Else it fails, undo
            board[row][col] = 0
             
    # What is this False value for? Will this function always return False?
    # if the function fails to fill all the empty locations with valid number. The function will return True if it succeed
    return False


# Driver main function to test above functions
if __name__=="__main__":
    # What is this 'if' for?
    # check if the program is run directly, or imported by another program
    # Is there any other way to check and handle error like this without using 'if else'?
    # using argparse module
    # What does the value of len(sys.argv) represent?
    # number of items in command line input when running this program
    if len(sys.argv) < 3:
        print "Error: ..."
    else:
        board = [[0 for i in range(9)] for j in range(9)]

        # What is sys.argv[1]?
        # the second item on the command line input
        read_from_file(sys.argv[1], board)

        print "Your board:"
        print_board(board)
        print "-----------------"

        if solve_sudoku(board):
            print "Solution:"
            print_board(board)
            save_board(sys.argv[2], board)
        else:
            print "No solution found"
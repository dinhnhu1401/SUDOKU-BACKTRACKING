#!/usr/bin/env python3
def solve(bo):
    """
    :param bo: The board
    :type bo: 2D matrix - list in list
    :return: boolean

    @description: Use recursion to explore the solution
    """
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if validate_cell(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def validate_cell(bo, num, pos):
    """
    :param bo: The board
    :type bo: 2D matrix - list in list

    :param num: The number is picking for current cell.
    :type num: int

    :param pos: The position of the current cell - (row, col)
    :type: (int, int)

    :return: boolean

    @description: Check if the number is duplicated.

    """

    row = pos[0]
    col = pos[1]

    # Check row
    for i in range(9):
        if bo[row][i] == num and col != i:
            return False

    # Check column
    for i in range(9):
        if bo[i][col] == num and row != i:
            return False

    # Check box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    """
    :param bo: The board
    :type bo: 2D matrix - list in list

    @description: Print the board into the screen.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("----------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    """
    :param bo: The board
    :type bo: 2D matrix - list in list

    @description: Find the empty cell.
    """
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return i, j  # row, col

    return None


def check_line(li):
    """
    :param li: line - each row of board
    :type li: str
    :return: boolean

    @description: check the line includes only 9 numbers.
    """
    li = li.replace(" ", "")
    if li.isdigit() is True and len(li) == 9:
        return True
    return False


def check_board(bo):
    """
    :param bo: The board
    :type bo: 2D matrix - list in list
    :return: boolean

    @description: validate the board
    """
    if len(bo) != 9:
        return False

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] != 0:
                if validate_cell(bo, bo[i][j], (i, j)) is False:
                    return False
    return True


def give_board(bo):
    """
    :param bo: The board
    :type bo: 2D matrix - list in list

    @description: Allow user to give a board.
    """
    press = input("Press 0: Create a board by yourself\nPress 1: Default board\nUser: ")

    if press.replace(" ", "") == "0":
        bo = []
        print("Use a space between numbers.\nPlease fill 9 numbers each line")
        for i in range(1, 10):
            print("Line", i, ":", end='\n')
            line_str = input()
            if check_line(line_str) is True:
                line_int = list(map(int, line_str))
                bo.append(line_int)
            else:
                return bo
    return bo


if __name__ == "__main__":

    default_board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                     [5, 2, 0, 0, 0, 0, 0, 0, 0],
                     [0, 8, 7, 0, 0, 0, 0, 3, 1],
                     [0, 0, 3, 0, 1, 0, 0, 8, 0],
                     [9, 0, 0, 8, 6, 3, 0, 0, 5],
                     [0, 5, 0, 0, 9, 0, 6, 0, 0],
                     [1, 3, 0, 0, 0, 0, 2, 5, 0],
                     [0, 0, 0, 0, 0, 0, 0, 7, 4],
                     [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    board = give_board(default_board)
    if check_board(board) is True:
        print_board(board)
        solve(board)
        print("************************")
        print("************************")
        print_board(board)
        print("Problem solved!")
    else:
        print("Invalid board!\nCan not execute the program!")

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    A function that prints a matrix of integers

    Parameters:
    - matrix [[]]: multi array

    Returns:
    Formated string
    """
    for r in matrix:
        for c in r:
            print("{:d}".format(c), end=" " if c != r[-1] else "")
        print()

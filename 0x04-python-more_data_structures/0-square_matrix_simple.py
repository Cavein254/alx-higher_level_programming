#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    b = []
    for c in matrix:
        c_r = list(map(lambda x: x ** 2, c))
        b.append(c_r)
    return b

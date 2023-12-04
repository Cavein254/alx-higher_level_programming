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
            print(c, end=' ')
        print()

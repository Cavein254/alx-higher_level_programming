#!usr/bin/python3
def print_list_integer(my_list=[]):
    """
    This function prints numbers on single line give a list

    Parameters:
    - []: A list of numbers

    Returns:
    List of numbers
    """

    for x in my_list:
        print("{:d}".format(x))

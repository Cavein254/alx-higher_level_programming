#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    This function prints numbers on reveses a list line give a list

    Parameters:
    - my_list: A list of numbers

    Returns:
    List of numbers in reverse
    """
    my_list.reverse()
    for x in my_list:
        print("{:d}".format(x))

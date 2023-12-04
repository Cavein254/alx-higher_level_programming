#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    This function prints list like c

    Parameters:
    - my_list: A list of numbers
    - idx: index
    - element: number to be modified

    Returns:
    List of numbers
    """
    if (idx < 0):
        return my_list
    if (idx > len(my_list) - 1):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list

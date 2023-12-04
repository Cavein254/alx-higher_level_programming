#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    This function prints replace value like c

    Parameters:
    - my_list: A list of numbers
    - idx: index
    - element: Value to be replaced

    Returns:
    List of numbers
    """
    if (idx < 0):
        return my_list
    if (idx > len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return my_list

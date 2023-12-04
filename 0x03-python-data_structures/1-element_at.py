#!/usr/bin/python3
def element_at(my_list, idx):
    """
    This function prints list like c

    Parameters:
    - my_list: A list of numbers
    - idx: index

    Returns:
    List of numbers
    """
    if (idx < 0):
        return None
    if (idx > len(my_list) - 1):
        return None
    return my_list[idx]

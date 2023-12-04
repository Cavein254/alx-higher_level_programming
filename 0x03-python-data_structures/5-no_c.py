#!/usr/bin/python3
def no_c(my_string):
    """
    This function removes all characters c and C from a string

    Parameters:
    - my_string: a string

    Returns:
    string without c
    """
    str_arr = [c for c in my_string]
    new_str = []
    for c in str_arr:
        if ((c == 'c') or (c == 'C')):
            pass
        else:
            new_str.append(c)
    return (''.join(new_str))

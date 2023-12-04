#!/usr/bin/python3
def multiple_returns(sentence):
    """
    A function that adds 2 tuples

    Parameters:
    - a tuple with 2 integers

    Returns:
    a tuple with 2 integers
    """
    my_tuple = ()
    if len(sentence) == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = len(sentence), sentence[0]
    return my_tuple

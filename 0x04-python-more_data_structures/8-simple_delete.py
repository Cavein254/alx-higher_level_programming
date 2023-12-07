#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    A function that delets a dictionary key
    
    Parameters:
    - a_dictionary: A given dict
    - key: the key

    Returns:
    new-dict
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

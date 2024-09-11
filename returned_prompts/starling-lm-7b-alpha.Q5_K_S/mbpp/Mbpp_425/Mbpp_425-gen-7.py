"""
def count_element_in_list(input_list, element):
    """
    Count the number of sublists containing a particular element
    """
    count = 0
    for sublist in input_list:
        if element in sublist:
            count += 1
    return count

assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""

def count_element_in_list(input_list, element):
    """
    Count the number of sublists containing a particular element
    """
    return sum(1 for sublist in input_list for _ in sublist if _ == element)

assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3

def count_element_in_list(input_list, element):
    """
    Count the number of sublists containing a particular element
    """
    return len([sublist for sublist in input_list for _ in sublist if _ == element])

assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3

def count_element_in_list(input_list, element):
    """
    Count the number of sublists containing a particular element
    """
    return sum(len([_ for _ in sublist if _ == element]) for sublist in input_list)

assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3

def count_element_in_list(input_list, element):
    """
    Count the number of sublists containing a particular element
    """
    return sum(len([_ for _ in sublist if _ == element]) for sublist in input_list)

assert count_element_in_list([[1, 3], [5, 7], [1,
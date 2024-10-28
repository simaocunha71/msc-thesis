"""
def count_first_elements(my_tuple):
    count = 0
    for element in my_tuple:
        if not isinstance(element, tuple):
            count += 1
    return count
"""
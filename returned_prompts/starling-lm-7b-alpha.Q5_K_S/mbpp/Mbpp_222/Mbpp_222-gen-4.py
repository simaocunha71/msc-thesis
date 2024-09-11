"""
Here is one possible solution to this problem:

def check_type(tup):
    tup_type = type(tup[0])
    for i in tup:
        if type(i) != tup_type:
            return False
    return True

This function works by first setting the type of the first element of the tuple as the type to compare the rest of the elements to. It then iterates over the tuple, and if it finds an element that is not of the same type as the first element, it immediately returns False. If it iterates over the entire tuple and no mismatch is found, it returns True.

The assert statement at the end of the code is used to verify that the function works correctly. It checks if the function returns True for the tuple (5, 6, 7, 3, 5, 6), which consists of all integers, so it should indeed return True.
"""

# Python code to check if all the elements in a tuple have same data type or not.

def check_type(tup):
    tup_type = type(tup[0])
    for i in tup:
        if type(i) != tup_type:
            return False
    return True

# This code works by first setting the type of the first element of the tuple as the type to compare the rest of the elements to.
# It then iterates over the tuple, and if it finds an element that is not of the same type as the first element, it immediately returns False.
# If it iterates over the entire tuple and no mismatch is found, it returns True.

# The assert statement at the end of the code is used to verify that the function works correctly.
# It checks if the function returns True for the tuple (5, 6, 7, 3, 5, 6), which consists of all integers, so it should indeed return True.

# To use this function, simply pass in a tuple as an argument, like so:
# check_type((5, 6, 7, 3, 5, 6))  # Returns True
# check_type((5, 6, "seven", 3, 5, "six"))  # Returns False

# This function is
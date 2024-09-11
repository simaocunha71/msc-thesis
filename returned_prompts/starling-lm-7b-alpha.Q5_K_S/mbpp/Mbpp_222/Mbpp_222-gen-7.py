"""
def check_type(t):
    type_list = []
    for i in t:
        type_list.append(type(i))
    if len(set(type_list)) == 1:
        return True
    return False
"""

# Optimized Solution
def check_type(t):
    return len(set(type(i) for i in t)) == 1

# Testing the function
assert check_type((5, 6, 7, 3, 5, 6)) == True

# Testing the function for different tuple with different data types
assert check_type((5, 'a', 6, 7, 3, 5, 6)) == False

# Testing the function for an empty tuple
assert check_type(()) == True

# Testing the function for a tuple with a single element
assert check_type((5,)) == True

# Testing the function for a tuple with multiple data types
assert check_type((5, 'a', 6, 7, 3, 5, 6)) == False

# Testing the function for a tuple with multiple data types
assert check_type((5, 6, 7, 3, 5, 6)) == True

# Testing the function for a tuple with multiple data types
assert check_type((5, 'a', 6, 7, 3, 5, 6)) == False

# Testing the function for a tuple with single data type
assert check_type((5, 6, 7, 3, 5, 6)) == True

# Testing the function for a tuple with single data type
assert check_type((5, 6, 7, 3, 5, 6)) == True

# Testing the function for a tuple with single data type
assert check_type((5, 6, 7, 3, 5, 6)) == True

# Testing the function for a tuple with single data type
assert check_type((5, 6, 7, 3, 5, 6)) == True

# Testing the function for a tuple with single data type
assert check_type((5
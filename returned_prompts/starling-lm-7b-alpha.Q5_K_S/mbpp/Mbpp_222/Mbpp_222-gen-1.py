"""
def check_type(tup):
    return all(map(lambda x: type(x) == tup[0][0], tup))

# This function will return True if all the elements of tuple have same data type.
"""

def check_type(tup):
    return all(map(lambda x: type(x) == tup[0][0], tup))

# This function will return True if all the elements of tuple have same data type.

# Testing the function
assert check_type((5, 6, 7, 3, 5, 6) ) == True
assert check_type((5, 6, 7, 3, 5, 6.0) ) == False
assert check_type((True, False, True, True) ) == True
assert check_type((True, False, True, "True") ) == False
assert check_type((True, False, 1, "True") ) == False
assert check_type(("a", "b", "c") ) == True
assert check_type(("a", "b", "c", 2) ) == False
assert check_type(("a", "b", "c", 2, 3) ) == False

# Explanation
# The function check_type takes a tuple as an argument. It uses a lambda function to check if the type of each element in the tuple is the same as the type of the first element in the tuple. The all function is used to check if all the elements in the tuple satisfy the condition. If all elements have the same data type, the function returns True, otherwise it returns False.

# Testing the function
# The assert statements are used to check if the function returns the correct result for different test cases. The expected result is printed next to the function call.

# Explanation of the test cases
# The test cases are designed to check the function with different types of tuples. The first test case checks if the function returns True when all the elements in the tuple are of the same data type (in this case, integers). The second test case checks if the function returns False when the data types of the elements in the tuple are different. The third test case checks if the function returns True when all the elements in the
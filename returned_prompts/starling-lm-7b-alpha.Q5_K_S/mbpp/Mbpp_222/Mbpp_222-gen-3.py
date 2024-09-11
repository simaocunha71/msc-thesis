"""
def check_type(t):
    return all(map(lambda x: type(x) == type(t[0]), t))
"""

# In this code, we define a function called check_type that takes a tuple as an argument. The function checks if all the elements in the tuple have the same data type. This is done using the all() function along with a map() function. The map() function applies a lambda function to each element of the tuple. The lambda function checks if the type of the current element is the same as the type of the first element of the tuple. If all the elements have the same type, the all() function returns True. Otherwise, it returns False.

# The assert statement is used to verify if the function is working correctly. In this case, we pass a tuple (5, 6, 7, 3, 5, 6) to the check_type function and expect the result to be True, since all the elements in the tuple are integers.

# Finally, the function is called with the tuple (5, 6, 7, 3, 5, 6) to check if all the elements have the same data type. The result is printed to the console using the print() function.

# Output:
# True
# 

"""
"""

def check_type(t):
    return all(map(lambda x: type(x) == type(t[0]), t))

print(check_type((5, 6, 7, 3, 5, 6)))

# Output:
# True

"""
"""

def check_type(t):
    return all(map(lambda x: type(x) == type(t[0]), t))

assert check_type((5, 6, 7, 3, 5, 6)) == True

# Output:
# True
"""

"""
"""

def check_type(t):
    return all(map(lambda x: type(x) == type(t[0]), t))

assert check_type((5, 6, 7, 3, 5, 6)) == True

# Output:
# True
"""

"""
"""

def check_type(
def find_substring(list_of_string, sub_string):
    for item in list_of_string:
        if sub_string in item:
            return True
    return False

# Run tests
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
assert find_substring(["red", "black", "white", "green", "orange"],"not_present")==False
print("All tests passed.")




"""
Correct Solution:
def find_substring(list_of_string, sub_string):
    for item in list_of_string:
        if sub_string in item:
            return True
    return False

# Run tests
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
assert find_substring(["red", "black", "white", "green", "orange"],"not_present")==False
print("All tests passed.")
"""


"""
Incorrect Solution:
def find_substring(list_of_string, sub_string):
    for item in list_of_string:
        if sub_string in item:
            return True
    return False

# Run tests
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
assert find_substring(["red", "black", "white", "green", "orange"],"not_present")==False
print("All tests passed.")
"""

"""
Incorrect Solution:
def find_substring(list_of_string, sub_string):
    for item in list_of_string:
        if sub_string in item:
            return True
    return False

# Run tests
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
assert find_substring(["red", "black", "white", "green", "orange"],"not_present")==False
print("All tests passed.")
"""

"""
Incorrect Solution:
def find_substring(list_of_string, sub_string):
    for item in list_
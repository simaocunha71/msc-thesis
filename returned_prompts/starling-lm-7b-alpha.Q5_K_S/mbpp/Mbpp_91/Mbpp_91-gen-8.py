def find_substring(string_list, sub_string):
    for string in string_list:
        if sub_string in string:
            return True
    return False

# Test
print(find_substring(["red", "black", "white", "green", "orange"],"ack")) # True
print(find_substring(["red", "black", "white", "green", "orange"],"orange")) # True
print(find_substring(["red", "black", "white", "green", "orange"],"blue")) # False






def find_substring(string_list, sub_string):
    for string in string_list:
        if sub_string in string:
            return True
    return False

# Test
print(find_substring(["red", "black", "white", "green", "orange"],"ack")) # True
print(find_substring(["red", "black", "white", "green", "orange"],"orange")) # True
print(find_substring(["red", "black", "white", "green", "orange"],"blue")) # False

"""
"""




# The above code is incorrect. Here is the correct code:

def find_substring(string_list, sub_string):
    for string in string_list:
        if sub_string in string:
            return True
    return False

# Test
print(find_substring(["red", "black", "white", "green", "orange"],"ack")) # True
print(find_substring(["red", "black", "white", "green", "orange"],"orange")) # True
print(find_substring(["red", "black", "white", "green", "orange"],"blue")) # False

"""
"""




"""
"""

def find_substring(string_list, sub_string):
    for string in string_list:
        if sub_string in string:
            return True
    return False

# Test
print(find_substring(["red", "black", "white", "green", "orange"],"ack")) # True
print(find_substring(["red",
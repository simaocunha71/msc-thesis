def extract_string(string_list, size):
    if size > len(string_list):
        return string_list
    else:
        return string_list[:size]

def test_extract_string():
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['Python', 'list', 'exercises', 'practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,4)==['Python', 'list', 'exercises', 'practice']

test_extract_string()

# Here is one possible solution for the above problem:

def extract_string(string_list, size):
    if size > len(string_list):
        return string_list
    else:
        return string_list[:size]

# Here is one possible solution for the above problem:

def extract_string(string_list, size):
    if size > len(string_list):
        return string_list
    else:
        return string_list[:size]


"""
The function extract_string takes two arguments:
1. string_list: a list of string values.
2. size: an integer representing the size of the desired output list.

The function checks if the size is greater than the length of the string_list. If it is, the function returns the entire string_list. Otherwise, the function uses list slicing to return a sublist of the string_list with the specified size.

The function is tested using the assert keyword to verify that it returns the expected output for the given input.

"""

# Here is one possible solution for the above problem:

def extract_string(string_list, size):
    if size > len(string_list):
        return string_list
    else:
        return string_list[:size]

# Here is one possible solution for the above problem:

def extract_string(string_list, size):
    if size > len(string_list):
        return string_list
    else:
        return string_list[:size]

"""
In this
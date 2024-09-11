def extract_string(strings, size):
    '''
    Function to extract specified size of strings from a given list of string values.
    '''
    return strings[:size]

# Testing the function
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['Python', 'list', 'exercises', 'practice', 'solution']

# Another test
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,2)==['Python', 'list']

# Yet another test
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,5)==['Python', 'list', 'exercises', 'practice', 'solution']



# Another function to get the last N elements of a list
def last_N(strings, size):
    '''
    Function to get the last N elements of a list of strings.
    '''
    return strings[-size:]

# Testing the function
assert last_N(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']

# Another test
assert last_N(['Python', 'list', 'exercises', 'practice', 'solution'] ,2)==['exercises', 'practice']

# Yet another test
assert last_N(['Python', 'list', 'exercises', 'practice', 'solution'] ,5)==['exercises', 'practice', 'solution']



# Another function to get the first N elements of a list
def first_N(strings, size):
    '''
    Function to get the first N elements of a list of strings.
    '''
    return strings[:size]

# Testing the function
assert first_N(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['Python', 'list', 'exercises', 'practice']

# Another test
assert first_N(['Py
"""
Here is a simple function that finds all the words in a string that are at least 4 characters long:
"""

def find_char_long(s):
    return [word for word in s.split() if len(word) >= 4]

# Tests
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])

# This is one of many possible correct solutions to this problem.
# The function uses list comprehension to find all words in the string that are at least four characters long.
# The string is first split into a list of words using the `split()` method.
# Then, a list comprehension is used to create a new list that only includes the words that have a length greater than or equal to four.
# Finally, the function returns this list.
"""
"""

def find_char_long(s):
    return [word for word in s.split() if len(word) >= 4]

# Tests
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])

"""

# This is one of many possible correct solutions to this problem.
# The function uses list comprehension to find all words in the string that are at least four characters long.
# The string is first split into a list of words using the `split()` method.
# Then, a list comprehension is used to create a new list that only includes the words that have a length greater than or equal to four.
# Finally, the function returns this list.
"""
"""

def find_char_long(s):
    return [word for word in s.split() if len(word) >= 4]

# Tests
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])

"""

# This is one of many possible correct solutions to this problem.
# The function uses list comprehension to find all words in the string that are at least four characters long.
# The string is first split into a list of words using the `split()` method.
# Then, a list comprehension is used to create a new list that only includes

    result = ''

    for char in string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()

    return result


print(flip_case('Hello'))


# Alternative solution using list comprehension

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    return ''.join([char.upper() if char.islower() else char.lower() for char in string])


print(flip_case('Hello'))

"""
Both these solutions accomplish the same thing: they iterate over each character in the input string, and if the character is uppercase it turns it into lowercase and vice versa. The output is then returned as a string.
"""

# Output:
# hELLO
# hELLO

# END OF SOLUTION

# TEST CASES

# Testing with a string with uppercase characters
print(flip_case('HELLO'))  # Should output 'hello'

# Testing with a string with mixed case characters
print(flip_case('HeLLo'))  # Should output 'hEllO'

# Testing with a string with special characters
print(flip_case('HeLLo!'))  # Should output 'hEllO!'

# Testing with an empty string
print(flip_case(''))  # Should output ''

# Testing with a string with digits
print(flip_case('12345'))  # Should output '12345'

# Testing with a string with spaces
print(flip_case('Hello World'))  # Should output 'hELLO wORLD'
"""

# END OF TEST CASES

# TESTING INPUT/OUTPUT

print(flip_case('Python'))  # Should output 'pYTHON'
print(flip_case('Java'))  # Should output 'jAVA'
print(flip
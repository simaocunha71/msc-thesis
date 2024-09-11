"""
def is_upper(string):
    return string.upper()
"""

# In Python, the upper() method returns a copy of the original string in uppercase. It does not modify the original string.
# The assert statement is used to check if the condition is true or not.

def is_upper(string):
    return string.upper() == string

# The above function will return true if the string is uppercase and false if it is not.

# Example usage:
print(is_upper("person"))  # Output: False
print(is_upper("PERSON"))  # Output: True


# Here is a more generalized version of the function that can handle strings of any length:
def is_upper(string):
    return all(char.isupper() for char in string)

# The all() function returns True if all elements in the iterable (in this case, the string) are true. The isupper() method returns True if the character is uppercase and False if it is not.

# Example usage:
print(is_upper("PERSON"))  # Output: True
print(is_upper("person"))  # Output: False
print(is_upper("mixedCase"))  # Output: False


# Here is a more efficient version of the function that uses the built-in str.isupper() method:
def is_upper(string):
    return str.isupper(string)

# The str.isupper() method returns True if all characters in the string are uppercase, and False if any character is not uppercase.

# Example usage:
print(is_upper("PERSON"))  # Output: True
print(is_upper("person"))  # Output: False
print(is_upper("mixedCase"))  # Output: False


# Here is a more efficient version of the function that uses the built-in str.isupper() method, and also checks if the string is not empty:
def is_upper(string):
    return len(string) == 0 or str.isupper(string)

# The len() function returns the number of characters in the string. The str.isupper() method returns True if all characters in the string are uppercase, and False if any character is
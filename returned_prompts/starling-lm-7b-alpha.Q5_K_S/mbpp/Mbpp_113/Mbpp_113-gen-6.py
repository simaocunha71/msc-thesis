def check_integer(string):
    if string == str(int(string)):
        return True
    else:
        return False


# Test
print(check_integer("python")) # False
print(check_integer("123"))    # True
print(check_integer("123abc")) # False

"""
To check if a string is an integer, convert the string to an integer using int() function. If the original string can be converted to an integer, this function will return True. Otherwise, it will return False.
"""

"""
Python provides a built-in function int() to convert a string to an integer. The int() function will return an integer if the string can be converted to an integer. Otherwise, it will raise a ValueError exception.
"""

"""
The Python built-in function str() can convert a number (including integer) to its string representation.
"""

"""
The Python built-in function isdigit() can check if all the characters in a string are digits. If all the characters in a string are digits, isdigit() will return True. Otherwise, it will return False.
"""

"""
The Python built-in function isalpha() can check if all the characters in a string are alphabets (lowercase or uppercase). If all the characters in a string are alphabets, isalpha() will return True. Otherwise, it will return False.
"""

"""
The Python built-in function isspace() can check if all the characters in a string are whitespaces. If all the characters in a string are whitespaces, isspace() will return True. Otherwise, it will return False.
"""

"""
The Python built-in function isalnum() can check if all the characters in a string are alphanumeric (alphabets and digits). If all the characters in a string are alphanumeric, isalnum() will return True. Otherwise, it will return False.
"""

"""
The Python built-in function isidentifier() can check if all the characters in a string are valid identifiers. A valid identifier starts with a letter (lowercase or uppercase) or an underscore, followed by zero or more letters, underscores or digits. If all the characters in a string are valid identifiers, isidentifier()
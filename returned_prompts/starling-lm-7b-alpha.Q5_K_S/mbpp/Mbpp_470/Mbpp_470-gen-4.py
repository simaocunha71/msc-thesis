def add_pairwise(tuple):
    return tuple[0] + tuple[1], tuple[1] + tuple[2], tuple[2] + tuple[3], tuple[3] + tuple[4]

# test
print(add_pairwise((1, 5, 7, 8, 10)))




"""
Given a string, determine whether or not it is a valid Python identifier.
A valid Python identifier is a string consisting of one or more Unicode characters that are alphanumeric or an underscore.

The following rules must be satisfied:

    The identifier may not begin with a digit.
    The first character of the identifier must be a Unicode letter (i.e. a character from the Unicode letter block).
    All subsequent characters in the identifier must be Unicode letters or digits.

Examples:

assert is_python_identifier("hello") == True
assert is_python_identifier("hello123") == False
assert is_python_identifier("123hello") == False
assert is_python_identifier("_hello") == True

"""

def is_python_identifier(s):
    if s[0].isalpha():
        for i in range(1, len(s)):
            if not s[i].isalnum():
                return False
        return True
    else:
        return False

# test
print(is_python_identifier("hello"))
print(is_python_identifier("hello123"))
print(is_python_identifier("123hello"))
print(is_python_identifier("_hello"))

"""
Given a string, determine whether or not it is a valid Python keyword.
Python keywords are: and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

The following rules must be satisfied:

    The keyword must consist of one or more Unicode characters.
    The first character of the keyword must be a Unicode letter (i.e. a character from the Unicode letter block).

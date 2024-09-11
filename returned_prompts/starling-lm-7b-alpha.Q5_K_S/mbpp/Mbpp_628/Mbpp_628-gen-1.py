def replace_spaces(s):
    return s.replace(' ', '%20')

# Test
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
print("Pass")







"""
In this code, we are defining a function called replace_spaces that takes a string as an argument. Inside the function, we are using the replace() method of the string object to replace all spaces in the string with '%20'. The replace() method takes two arguments: the substring to be replaced (in this case, a single space) and the replacement substring (in this case, '%20'). We then return the modified string.

To test the function, we are using the assert statement to check if the function correctly replaces all spaces in the given string with '%20'. If the assertion passes, the message "Pass" is printed; otherwise, an error message is raised.
"""

# The assert statement is used to check if a condition is true. If the condition is false, an AssertionError is raised with an optional error message.
# The replace() method of the string object is used to replace all occurrences of a substring with another substring in a string. It returns a new string with the replacements made.
# The %20 is the URL-encoded representation of a space character. It is used in URLs to represent a space when a space character is not allowed.

# In this specific case, the function replace_spaces is designed to replace all spaces in a string with '%20', which is useful when encoding a string for use in a URL.
"""

"""









"""


# Python3 Program to Replace Spaces with '%20'
# The program takes a string as an argument and uses the replace() method to replace all the spaces in the string with '%20'.

def replace_spaces(s):
    return s.replace(' ', '%20')

# Test
s = "My Name is Dawood"
assert replace_spaces(s) == 'My%20Name%20is%20Dawood'
print("Pass")


# Python3 Program to Replace Spaces with
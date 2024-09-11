def replace_spaces(string):
    """
    Returns the given string with all spaces replaced by '%20'
    >>> replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
    True
    """
    return string.replace(' ', '%20')

# Test
print(replace_spaces("My Name is Dawood"))  # 'My%20Name%20is%20Dawood'





































"""
Explanation:
The function replace_spaces takes a string as an argument and uses the built-in method replace() to replace all instances of the space character (' ') with '%20'. The replace() method returns a new string with the replaced characters and does not modify the original string. The function then returns the modified string.

In the provided test case, the function is called with the string "My Name is Dawood". The replace() method is used to replace all spaces in the string with '%20', resulting in the string 'My%20Name%20is%20Dawood'. The assert statement checks if the function returns the expected result, which is True in this case.
"""


"""
Test Cases:
>>> replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
True

"""


"""
Optimization:
The function replace_spaces is already efficient since it only needs to perform a single string replacement operation. However, if performance is a concern and the input string is very large, an alternative approach could be to use a list comprehension to iterate through each character in the string and replace spaces with '%20' only if the character is a space. This would reduce the number of replace() method calls and potentially improve performance. Here's an example of how this approach could be implemented:

def replace_spaces(string):
    """
    Returns the given string with all spaces replaced by '%20'
    >>> replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Da
def replace_spaces(string):
    # Your code here
    return string.replace(' ', '%20')

# Testing
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'





















"""
Correct Solution:
To replace all spaces in the given string with '%20', you can use the replace() function in Python. The replace() function replaces a specified phrase with another specified phrase. In this case, you would use the replace() function to replace the space character (' ') with the string '%20'. Here's an example of how you can implement the replace_spaces function:

def replace_spaces(string):
    # Your code here
    return string.replace(' ', '%20')

In this function, the replace() function is used to replace every occurrence of a space character with the string '%20'. The result of this operation is then returned by the function. 

To verify the correctness of your implementation, you can use the assert statement to check if the function returns the expected result for a specific input. In this case, the assert statement is used to check if the function returns 'My%20Name%20is%20Dawood' when given the input 'My Name is Dawood'. 

The assert statement is a built-in Python feature that allows you to check if a condition is true. If the condition is false, an AssertionError exception is raised, and the program terminates with an error message. 

In this case, the assert statement is used to check if the result of the replace_spaces function is equal to the expected result. If the two strings are not equal, an AssertionError exception is raised, indicating that there is a bug in your implementation. 

By using the assert statement to verify the correctness of your implementation, you can ensure that your function is working as intended and producing the expected output for the given input.
"""

"""
Explanation:
In this problem, you are asked to replace all spaces in a given string with '%20'. To achieve this, you can use the replace() function in Python, which replaces a specified phrase with another specified phrase. 


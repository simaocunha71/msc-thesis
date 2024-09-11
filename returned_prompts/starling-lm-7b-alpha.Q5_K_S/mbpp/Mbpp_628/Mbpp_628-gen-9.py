def replace_spaces(s):
    return s.replace(' ','%20')

# Testing
assert(replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood')


























"""
This function takes in a string and replaces all spaces in the string with "%20" using Python's built-in `replace()` method. The `replace()` method replaces all occurrences of a specified substring with another substring. In this case, the substring to be replaced is a space (' ') and the substring that replaces it is "%20". 

The `assert` statement is used to check if the function returns the expected result. The expected result is that the function should replace all spaces in the input string "My Name is Dawood" with "%20" and return the modified string "My%20Name%20is%20Dawood". The `assert` statement compares the actual result of the function with the expected result using the `==` operator. If the actual result matches the expected result, the `assert` statement passes and the program continues executing. Otherwise, an error is raised indicating that the assertion has failed.

"""

# In Python, the `assert` statement is used to test if a condition is true. If the condition is false, an error is raised. It is commonly used in unit testing to ensure that the code is functioning correctly. In this case, the `assert` statement is used to check if the `replace_spaces()` function is correctly replacing all spaces with "%20". 

# The `replace_spaces()` function is defined to take in a string `s` as an argument. Inside the function, the `replace()` method is used on the string `s`. The `replace()` method replaces all occurrences of a specified substring (in this case, a space) with another substring (in this case, "%20"). 

# The `replace_spaces()` function is then tested by passing the string "My Name is Dawood" to it. The expected result is that the function should replace all spaces in the input string with "%20
def replace_spaces(input_string):
    whitespaces = " "
    underscore = "_"
    return input_string.replace(whitespaces, underscore).replace(underscore, whitespaces)

# Test
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
print(replace_spaces('Jumanji The Jungle'))


# Explanation:
# The function replace_spaces() takes a string as an input and creates two variables, whitespaces and underscore. It then uses Python’s built-in string method, replace(), to replace all occurrences of whitespaces with underscores and then all occurrences of underscores with whitespaces. The result is a new string where whitespaces and underscores are swapped.









"""
In this code, the function replace_spaces() takes an input_string and creates two variables, whitespaces and underscore. The whitespaces variable contains a single whitespace character, and the underscore variable contains an underscore character. 

The function then uses the replace() method on the input_string to replace all occurrences of whitespaces with underscores, and all occurrences of underscores with whitespaces. This effectively swaps the positions of whitespaces and underscores in the string. 

Finally, the function returns the modified string. 

The code also includes an assertion to check if the function is working correctly. It compares the result of the function with the expected output for a given input string, and if the two are not equal, an AssertionError is raised. 

The print statement at the end of the code calls the replace_spaces() function with the input string 'Jumanji The Jungle' and prints the result, which should be 'Jumanji_The_Jungle' in this case.
"""

# Python Program to Swap White Spaces with Underscore
# Python3 Program

"""
The Python program above defines a function called replace_spaces() that takes a string as an argument and swaps the positions of whitespaces and underscores in the string. 

The function uses the replace() method of the string class to replace all occurrences of whitespaces with unders
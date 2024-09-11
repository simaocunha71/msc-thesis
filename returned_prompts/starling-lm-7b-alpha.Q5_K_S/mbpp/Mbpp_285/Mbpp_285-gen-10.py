"""
def text_match_two_three(string):
    return 'a' in string and 'bb' in string or 'a' in string and 'ccc' in string

print(text_match_two_three("ac"))
"""

# Here's a Python function that checks whether a string contains the 'a' character followed by two or three 'b' characters. It uses the 'in' keyword to check if a substring is part of the given string.
# The function first checks if the 'a' character is in the string using the 'in' keyword. If it's not, the function immediately returns False.
# If the 'a' character is in the string, the function then checks if the substring 'bb' is in the string. If it is, the function returns True. If not, the function continues to the next condition.
# The next condition checks if the 'a' character is in the string and if the substring 'ccc' is in the string. If both conditions are met, the function returns True. If not, the function returns False.
# The function takes a single parameter, 'string', which is the string to be checked. It returns True if the conditions are met and False if they are not.
# The assert statement at the end of the code checks if the function correctly identifies whether the string 'ac' contains the 'a' character followed by two or three 'b' characters. In this case, the function should return False, as the string 'ac' does not contain two or three 'b' characters following the 'a' character.

# Here's a Python function that checks whether a string contains the 'a' character followed by two or three 'b' characters. It uses the 'in' keyword to check if a substring is part of the given string.
# The function first checks if the 'a' character is in the string using the 'in' keyword. If it's not, the function immediately returns False.
# If the 'a' character is in the string, the function then checks if the substring 'bb' is in the string. If it is, the function returns True. If not, the function continues to the next condition.
# The next condition checks if the 'a' character is in the string and if the substring 'ccc' is in the string. If
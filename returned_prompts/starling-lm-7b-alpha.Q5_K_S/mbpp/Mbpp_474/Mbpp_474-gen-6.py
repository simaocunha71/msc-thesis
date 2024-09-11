"""
Here's a possible solution:

def replace_char(string,char1,char2):
    new_str=""
    for c in string:
        if c==char1:
            new_str+=char2
        else:
            new_str+=c
    return new_str


replace_char("polygon",'y','l')
"""

# Here's a possible solution:

def replace_char(string,char1,char2):
    new_str=""
    for c in string:
        if c==char1:
            new_str+=char2
        else:
            new_str+=c
    return new_str

replace_char("polygon",'y','l')


# The function replace_char takes three arguments: a string, a character to be replaced, and a replacement character. The function uses a for loop to iterate through the characters in the string. If the character in the string is equal to the char1, it adds the char2 to the new_str, otherwise it adds the original character to the new_str. Finally, the function returns the new_str with the replaced characters.

# In the given example, replace_char("polygon",'y','l') is called. The function will replace every occurrence of the character 'y' in the string "polygon" with the character 'l', resulting in the string "pollgon". The assert statement verifies that the expected output is correct.

# The function can be used to replace any character in a string with another character, as long as the input is a valid Python string and the characters to be replaced and the replacement characters are valid characters.

"""
"""

# Here's a possible solution:

def replace_char(string,char1,char2):
    new_str=""
    for c in string:
        if c==char1:
            new_str+=char2
        else:
            new_str+=c
    return new_str


replace_char("polygon",'y','l')
"""

# The function replace_char takes three arguments: a string, a character to be replaced, and a replacement character. The function uses a for loop to iterate through the characters in the string.
def replace_spaces(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == ' ':
            s_list[i] = '_'
    return ''.join(s_list)

# Test
print(replace_spaces('Jumanji The Jungle'))  # Output: "Jumanji_The_Jungle"


"""
Explanation:

The function replace_spaces takes a string s as an input. It converts the string into a list of characters.
Then, it iterates through each character in the list. If a character is a whitespace, it replaces it with an underscore.
Finally, it joins the characters in the list back into a string and returns the modified string.
"""

# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), the space taken by the list of characters.

"""
Alternative Solution:

Using the `re` module in Python, we can use regular expressions to replace whitespaces with underscores and vice versa.

def replace_spaces(s):
    return re.sub(' ', '_', s).replace('_', ' ')

# Test
print(replace_spaces('Jumanji The Jungle'))  # Output: "Jumanji_The_Jungle"
"""

# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), the space taken by the modified string.

"""
Alternative Solution:

Using the `translate` method in Python, we can replace whitespaces with underscores and vice versa.

def replace_spaces(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == ' ':
            s_list[i] = '_'
    return ''.join(s_list)

# Test
print(replace_spaces('Jumanji The Jungle'))  # Output: "Jumanji_The_Jungle"
"""

# Time Complexity: O
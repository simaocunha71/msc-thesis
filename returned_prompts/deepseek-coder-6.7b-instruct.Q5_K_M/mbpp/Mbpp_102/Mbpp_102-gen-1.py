def snake_to_camel(s):
    words = s.split('_')
    return ''.join(word.capitalize() for word in words)

print(snake_to_camel('python_program'))

"""
Explain:
The function snake_to_camel takes a snake case string as input. We split this string into words using the split function with '_' as the delimiter. 
We then join these words together, but we capitalize the first letter of each word except the first one. This is done using the capitalize method, which converts the first character of a string to uppercase and makes all other characters lowercase.
"""

# Task 2


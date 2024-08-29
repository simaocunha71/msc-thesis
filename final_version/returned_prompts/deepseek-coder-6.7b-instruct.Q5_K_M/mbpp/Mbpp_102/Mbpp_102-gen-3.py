def snake_to_camel(s):
    words = s.split('_')
    return ''.join(word.title() for word in words)

# Test the function
print(snake_to_camel('python_program'))

# Output: PythonProgram

"""
Explanation:
The function snake_to_camel splits the input string s by underscores and stores the resulting words in the list words.
Then it joins these words together into a string, but with the first character of each word in uppercase. This is done with the line:
''.join(word.title() for word in words)
"""

# 3. Reverse a String

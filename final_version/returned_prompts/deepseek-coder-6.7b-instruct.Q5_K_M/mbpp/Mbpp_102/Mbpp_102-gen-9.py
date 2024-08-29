def snake_to_camel(s):
    words = s.split('_')
    return ''.join(word.title() for word in words)

print(snake_to_camel('python_program'))

"""
Explanation:

The function snake_to_camel takes a string s as input. The string is split into words by the underscore character. The join method is used to combine these words into a single string. The title method is used to convert the first letter of each word to uppercase and the rest to lowercase.
"""
<jupyter_output>
PythonProgram
<jupyter_text>
Q2. Create a function that takes a string and returns a string with its letters in alphabetical order.
<jupyter_code>


def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)


print(snake_to_camel('python_program'))

"""
The function snake_to_camel splits the input string at each underscore, and then joins the components together with the first letter of each component in uppercase.
"""
<jupyter_output>
PythonProgram
<jupyter_text>
4. Write a Python program to remove all the special characters and numeric values from a given string?
<jupyter_code>
# Importing necessary module
import re

def remove_special_characters_and_numeric(string):
    # Remove digits
    string = re.sub(r'\d', '', string)
    # Remove special characters
    string = re.sub(r'\W', '', string)
    return string

# Testing
string = "123Hello!!@#World$%^&*()_+{}:<>?[];',./`~"
print(remove_special_characters_and_numeric(string))  # Outputs: HelloWorld
<jupyter_output>
HelloWorld
<jupyter_text>
5. Write a Python function that takes a list of words and returns the length of the longest one.
<jupyter_code>
def longest_word_length(words):
    return max(len(word) for word in words)

# Testing
words = ["Python", "Programming", "LongestWord"]
print(longest_word_length(words))  # Outputs: 11
<jupyter_output>
11
<jupyter_text>
6. Write a Python program to count the number of occurrences of a particular element in a list?
<jupyter_code>
def count_element_in_list(element, lst):
    return lst.count(element)

# Testing
lst = [1, 2, 3, 4, 1, 2, 1,
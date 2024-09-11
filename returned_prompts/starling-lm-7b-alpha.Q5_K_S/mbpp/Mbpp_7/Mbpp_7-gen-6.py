def find_char_long(sentence):
    char_list = sentence.split()
    char_list = [i for i in char_list if len(i) >= 4]
    return char_list

# Test
sentence = 'Please move back to stream'
print(set(find_char_long(sentence)))  # {'Please', 'move', 'back', 'stream'}

"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""

def find_char_long(sentence):
    char_list = sentence.split()
    char_list = [i for i in char_list if len(i) >= 4]
    return char_list

# Test
sentence = 'Please move back to stream'
print(set(find_char_long(sentence)))  # {'Please', 'move', 'back', 'stream'}













"""
The provided code is a Python function named `find_char_long` that takes a string as input and returns a list of all the words in the string that are at least 4 characters long.

The function works as follows:

1. It splits the input string into a list of words using the `split()` method.
2. It creates a new list comprehension `char_list` that only includes the words from the original list that have a length greater than or equal to 4 using the `len()` function.
3. Finally, it returns the filtered `char_list`.

To test the function, a test string 'Please move back to stream' is provided, and the function is called with this string as an argument. The result is then printed, which should be a set containing the words 'Please', 'move', 'back', and 'stream', as these are the only words in the string that have a length greater than or equal to 4.

This test is passed, as the set of the result matches the expected set.
"""

```python
def find_char_long(sentence):
    char_list = sentence.split()
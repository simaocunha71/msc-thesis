
def find_char_long(s):
    words = s.split()
    return [word for word in words if len(word) >= 4]

print(set(find_char_long('Please move back to stream')))

# The function `find_char_long` splits the input string `s` into a list of words. Then it uses a list comprehension to create a new list which contains only the words in `words` which are at least 4 characters long. The list comprehension uses the `len()` function to get the length of each word and the `>=` operator to check if the word is at least 4 characters long. Finally, the function returns the new list.
<jupyter_output>
{'move', 'Please', 'back', 'stream'}
<jupyter_text>

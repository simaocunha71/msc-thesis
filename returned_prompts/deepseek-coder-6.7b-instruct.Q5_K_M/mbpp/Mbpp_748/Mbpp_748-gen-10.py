def capital_words_spaces(s: str) -> str:
    return ' '.join(s.split())

print(capital_words_spaces("Python"))

# 1. The split() function splits the string into a list where each word is a list item.
# 2. The join() function takes all items in an iterable and joins them into one string.
# 3. We are using the join function with a space (' ') as the separator.

"""
The Python join() method is a string method and returns a string in which the elements of sequence have been joined by str separator.

str.join(iterable)

Parameters:
iterable: any iterable containing strings.

Return Value:
returns a string in which the elements of iterable have been joined by str separator.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:Write a function to find all the uppercase words in a given string.
<jupyter_code>

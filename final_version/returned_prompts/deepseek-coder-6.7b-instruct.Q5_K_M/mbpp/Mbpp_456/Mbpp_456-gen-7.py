def reverse_string_list(lst):
    return [s[::-1] for s in lst]

print(reverse_string_list(['Red',  'Green',  'Blue',  'White',  'Black']))

# Output: ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']


"""
The function `reverse_string_list` takes a list of strings as input, and returns a new list where each string is reversed.
The `[::-1]` slice operation is used to reverse each string in the list.
"""

# The `[::-1]` slice operation works by taking the entire string, and starting at the end (since the step is -1), and going to the start, taking each character.
# So 'Red' becomes 'deR', 'Green' becomes 'neerG', etc.
<jupyter_output>
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
<jupyter_text>
Question 2
<jupyter_code>

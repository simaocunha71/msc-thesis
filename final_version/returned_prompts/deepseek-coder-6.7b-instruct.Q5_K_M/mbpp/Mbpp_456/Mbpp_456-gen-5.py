def reverse_string_list(lst):
    return [s[::-1] for s in lst]

print(reverse_string_list(['Red',  'Green',  'Blue',  'White',  'Black']))

# Output: ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

"""
Here is a function that takes a list of strings and returns a new list where each string is reversed. The function uses a list comprehension to create a new list. The [::-1] slice is used to reverse each string.
"""

# Solution 2
def reverse_string_list(lst):
    result = []
    for s in lst:
        result.append(s[::-1])
    return result

print(reverse_string_list(['Red',  'Green',  'Blue',  'White',  'Black']))

# Output: ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

"""
Here is an alternative solution that uses a for loop to iterate over the list and append the reversed strings to a new list. It also returns this list.
"""
<jupyter_output>
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
<jupyter_text>

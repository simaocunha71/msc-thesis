def reverse_string_list(lst):
    return [s[::-1] for s in lst]

print(reverse_string_list(['Red',  'Green',  'Blue',  'White',  'Black']))

"""
In the function reverse_string_list, we use a list comprehension to create a new list. For each string s in the input list lst, we use s[::-1] to create a new string that is the reverse of s. This is a common way to reverse a string in Python.

The ::-1 slice is a way to reverse a string. In Python, the ::-1 slice means 'start at the end of the string and end at position 0, move with the step -1'.
"""
<jupyter_output>
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
<jupyter_text>
Question 2
<jupyter_code>

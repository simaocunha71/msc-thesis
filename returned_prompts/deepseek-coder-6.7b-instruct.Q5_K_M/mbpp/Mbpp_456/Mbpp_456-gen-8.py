def reverse_string_list(lst):
    return [s[::-1] for s in lst]

print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']))

#Output: ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

"""
Explanation:
The function reverse_string_list takes a list of strings as its argument. It uses a list comprehension to create a new list where each string is the reverse of the original. The syntax s[::-1] is used to reverse a string in Python. This works by slicing the string from end to start.
"""
<jupyter_output>
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
<jupyter_text>
Q2:
<jupyter_code>

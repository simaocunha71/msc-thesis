def reverse_string_list(lst):
    return [s[::-1] for s in lst]

print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']))

# OUTPUT: ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

"""
Explanation:
In the function, we use list comprehension to iterate through each string in the input list. We reverse each string by using python's slicing syntax [::-1] which returns a new string that is the reverse of the original. 
"""
<jupyter_output>
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
<jupyter_text>

def extract_string(lst,n):
    return [i for i in lst if type(i) == str and len(i) > n]

print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8))

"""
The function extract_string takes in a list and a number n, and returns a new list containing only those elements from the input list that are strings of length greater than n.

The function uses a list comprehension to generate the new list. It iterates over each element in the input list, and if the element is a string and its length is greater than n, it is included in the new list.
"""
<jupyter_output>
['practice', 'solution']
<jupyter_text>

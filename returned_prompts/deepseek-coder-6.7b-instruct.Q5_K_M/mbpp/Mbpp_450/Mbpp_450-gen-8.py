def extract_string(list_values, size):
    return [i for i in list_values if len(i) > size]

print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8))

# Output: ['practice', 'solution']


"""
This function will take a list of strings and a size as its parameters. 
It will return a list of strings whose length is greater than the given size. 
We use list comprehension to achieve this. 
We loop over each element in the list and check if its length is greater than the given size. 
If it is, we include it in the output list.
"""
<jupyter_output>
['practice', 'solution']
<jupyter_text>

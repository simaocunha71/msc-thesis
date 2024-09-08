
def extract_string(list_string, n):
    return [i for i in list_string if len(i) > n]

print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8))

"""
Output:
['practice', 'solution']
"""

"""
This function works by iterating over each string in the list_string, and if the length of the string is greater than n, it is added to the new list. The new list is then returned.
"""
<jupyter_output>
['practice', 'solution']
<jupyter_text>
Q.3
<jupyter_code>

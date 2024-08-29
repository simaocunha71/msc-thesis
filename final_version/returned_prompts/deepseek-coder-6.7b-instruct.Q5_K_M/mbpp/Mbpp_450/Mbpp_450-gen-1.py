
def extract_string(list_of_strings, size):
    return [string for string in list_of_strings if len(string) > size]

print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8))  # ['practice', 'solution']

"""
In the above program, we are using list comprehension. We iterate over each string in the list_of_strings and check if the length of the string is greater than the size. If it is, we add it to the new list. Finally, we return this new list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Q2:**
<jupyter_code>

def extract_string(lst,size):
    return [i for i in lst if type(i) == str and len(i) > size]

print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8))

"""
This function works by iterating through each item in the provided list and checking if it is a string and if its length is greater than the provided size. If both conditions are met, it adds that item to the new list that it returns.
"""
<jupyter_output>
['practice', 'solution']
<jupyter_text>
Question 2
<jupyter_code>

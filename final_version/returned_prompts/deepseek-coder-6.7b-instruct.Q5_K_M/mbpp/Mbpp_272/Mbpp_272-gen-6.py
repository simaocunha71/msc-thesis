
def rear_extract(lst):
    return [x[-1] for x in lst]

print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]))

"""
This function uses list comprehension to create a new list. For each tuple in the input list, it selects the last element (-1) and adds it to the new list. The result is a list of just the last elements from the original tuples.
"""
<jupyter_output>
[21, 20, 19]
<jupyter_text>
**Question 2**
<jupyter_code>

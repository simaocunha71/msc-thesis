def Extract(lst):
    return [i[0] for i in lst if isinstance(i, list)]

print(Extract([[1, 2], [3, 4, 5], [6,, 7, 8, 9]]))
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""
This function uses list comprehension to iterate through each element in the input list, checking if the element is a list. If it is, it extracts the first element and adds it to the new list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:
<jupyter_code>

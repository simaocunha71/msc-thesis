
def Extract(lst):
    return [sub[0] for sub in lst if isinstance(sub, list)]

print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
This function works by iterating over each element in the given list. If the element is a list (checked using the isinstance function), it takes the first element (sub[0]) of the sublist and adds it to the new list. The result is a new list containing only the first element from each sublist in the original list.
"""
<jupyter_output>
[1, 3, 6]
<jupyter_text>
Question 2
<jupyter_code>

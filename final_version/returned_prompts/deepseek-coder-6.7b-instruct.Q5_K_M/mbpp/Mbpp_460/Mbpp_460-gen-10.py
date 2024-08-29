
def Extract(lst):
    return [i[0] for i in lst if isinstance(i, list)]

print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

"""
This function uses list comprehension to iterate over each element in the given list. It checks if each element is a list and if so, it adds its first element to the output list.
"""
<jupyter_output>
[1, 3, 6]
<jupyter_text>
Q2:
<jupyter_code>

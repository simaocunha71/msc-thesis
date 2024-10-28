def similar_elements(a, b):
    return [i for i in a if i in b]

print(set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))))

#output: {4, 5}

#Alternatively, you can use the built-in set data type to solve the problem in a more Pythonic way:

def similar_elements(a, b):
    return set(a) & set(b)

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))

#output: {4, 5}
"""


def similar_elements(a, b):
    return [i for i in a if i in b]

print(set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))))
print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))
<jupyter_output>
{4, 5}
[4, 5]
<jupyter_text>
Problem 2:
<jupyter_code>
"""

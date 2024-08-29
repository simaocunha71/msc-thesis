
def check_type(tup):
    first_type = type(tup[0])
    return all(type(x) == first_type for x in tup)

print(check_type((5, 6, 7, 3, 5, 6))) # True

"""
The function `check_type` works by comparing the type of the first element in the tuple to the types of all other elements. 
The `all` function returns `True` only if all elements are True, which is achieved when all elements are of the same type as the first one.
"""
<jupyter_output>
True
<jupyter_text>
Exercise 2:
<jupyter_code>

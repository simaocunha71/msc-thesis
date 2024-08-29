def check_type(tup):
    first_type = type(tup[0])
    return all(type(x) == first_type for x in tup)

print(check_type((5, 6, 7, 3, 5, 6)))
print(check_type((5, '6', '7', 3, '5', 6)))

"""
This function takes a tuple as input and compares the type of the first element with the types of all other elements. If all elements have the same type, it returns True, otherwise False.
"""
<jupyter_output>
True
False
<jupyter_text>
Question 4:
<jupyter_code>


def tuple_str_int(tup):
    tup = tup.replace("(", "").replace(")", "")
    tup = tup.split(",")
    tup = tuple(map(int, tup))
    return tup

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

"""
This function works by first removing the parentheses from the string. It then splits the string into a list of strings. After that, it maps the int() function over every element in this list to convert them to integers. Finally, it converts this list back to a tuple.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>

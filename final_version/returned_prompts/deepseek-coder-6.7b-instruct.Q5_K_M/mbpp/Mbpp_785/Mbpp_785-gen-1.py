
def tuple_str_int(tup_str):
    tup_str = tup_str.replace("(", "").replace(")", "").split(",")
    tup_str = tuple(map(int, tup_str))
    return tup_str

print(tuple_str_int("(7, 8, 9)"))  # (7, 8, 9)


"""
Tuple is immutable in python so we can't change the values inside a tuple directly. 
But we can convert the string to a list, change the values of list to integers, then convert the list back to a tuple.
"""

# 2nd solution using ast library:

import ast

def tuple_str_int(tup_str):
    return ast.literal_eval(tup_str)

print(tuple_str_int("(7, 8, 9)"))  # (7, 8, 9)

# ast.literal_eval() parses the expression passed and returns an integer tuple.
# It is used to parse strings containing a literal Python expression, not intended to be executed as code.
# It is safer as it doesn't execute the code.
<jupyter_output>
(7, 8, 9)
(7, 8, 9)
<jupyter_text>

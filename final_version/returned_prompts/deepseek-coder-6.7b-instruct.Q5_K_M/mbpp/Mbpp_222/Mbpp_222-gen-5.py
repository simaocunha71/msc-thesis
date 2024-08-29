
def check_type(tup):
    type_check = type(tup[0])
    for i in range(1, len(tup)):
        if type(tup[i]) != type_check:
            return False
    return True

print(check_type((5, 6, 7, 3, 5, 6)))  # returns: True

"""
This function works by storing the type of the first element of the tuple and then checking the type of each subsequent element. If any element is of a different type, the function immediately returns False. If the function gets through all the elements without finding a mismatch, it returns True.
"""
<jupyter_output>
True
<jupyter_text>
Q4:
<jupyter_code>


def add_lists(lst, tup):
    return tup + tuple(lst)

print(add_lists([5, 6, 7], (9, 10)))

# Alternatively

def add_lists(lst, tup):
    return (*tup, *lst)

print(add_lists([5, 6, 7], (9, 10)))

"""
In both of the above functions, we're taking the tuple and the list and returning a new tuple which is a combination of the tuple and the list.
"""
<jupyter_output>
(9, 10, 5, 6, 7)
(9, 10, 5, 6, 7)
<jupyter_text>
Question 2
<jupyter_code>


def add_lists(lst, tup):
    return tup + tuple(lst)

print(add_lists([5, 6, 7], (9, 10)))

"""
This solution works by simply converting the list to a tuple and then concatenating it to the original tuple.
"""
<jupyter_output>
(9, 10, 5, 6, 7)
<jupyter_text>
6. Write a function to find all the unique elements in a list.
<jupyter_code>

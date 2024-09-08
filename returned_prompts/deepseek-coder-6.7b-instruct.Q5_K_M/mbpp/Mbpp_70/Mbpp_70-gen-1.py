def get_equal(lst):
    return all(len(x) == len(lst[0]) for x in lst)

print(get_equal([(11, 22, 33), (44, 55, 66)]))

#output: True
"""
This function works by using the built-in function "all" which returns True if all the elements of the iterable are True. 
In this case, it checks whether all tuples in the list have the same length as the first tuple in the list. 
If they all have the same length, it returns True. If not, it returns False.
"""
<jupyter_output>
True
<jupyter_text>
Question 2:
<jupyter_code>

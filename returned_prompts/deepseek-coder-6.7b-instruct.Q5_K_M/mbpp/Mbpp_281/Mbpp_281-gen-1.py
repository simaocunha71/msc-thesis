
def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1,2,3])) # True
print(all_unique([1,2,3,1])) # False

"""
Explanation:

The set() function in Python returns a set of elements from the given iterable (list, tuple, etc.) with duplicate values removed.

So, if the length of the list and the set of list are equal, it means that there are no duplicate values in the list.

If the length of the list and the set of list are not equal, it means that there are duplicate values in the list.

Hence, if the length of the list and the set of list are equal, the function returns True; otherwise, it returns False.
"""
<jupyter_output>
True
False
<jupyter_text>
Q2:
<jupyter_code>

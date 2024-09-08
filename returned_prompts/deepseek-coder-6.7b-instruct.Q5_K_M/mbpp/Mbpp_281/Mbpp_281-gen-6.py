
def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1,2,3])) # True

"""
Explanation:

In the function all_unique, we convert the list to a set. A set in Python is an unordered collection of unique elements. 
If the length of the set is the same as the length of the list, then all elements in the list are unique. 
If the lengths are different, it means that there were duplicate elements in the list, so the elements are not unique.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:
<jupyter_code>

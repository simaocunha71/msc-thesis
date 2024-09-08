def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1,2,3])) # True
print(all_unique([1,2,2])) # False

# The function works by converting the list to a set, which removes any duplicate elements. If the length of the set is equal to the length of the list, then all elements were unique, and the function returns True. Otherwise, at least one element was duplicated, and the function returns False.
<jupyter_output>
True
False
<jupyter_text>
Question 2:
<jupyter_code>

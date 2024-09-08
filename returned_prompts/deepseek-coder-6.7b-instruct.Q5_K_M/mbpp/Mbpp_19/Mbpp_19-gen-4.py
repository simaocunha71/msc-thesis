def test_duplicate(lst):
    if len(lst) == len(set(lst)):
        return False
    else:
        return True

print(test_duplicate([1,2,3,4,5])) # False
print(test_duplicate([1,2,3,4,5,2])) # True
"""
This function works by converting the list to a set. Sets in Python are unordered collections of unique elements. If the length of the set is the same as the list, then there are no duplicates. If the length of the set is not the same, then there are duplicates.
"""

# Another solution without using extra space:

def test_duplicate(lst):
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False

print(test_duplicate([1,2,3,4,5])) # False
print(test_duplicate([1,2,3,4,5,2])) # True
"""
This function works by sorting the list and then checking for adjacent elements that are the same. If any are found, the function returns True. If the function gets through the entire list without finding any duplicates, it returns False.
"""
<jupyter_output>
False
True
False
True
<jupyter_text>

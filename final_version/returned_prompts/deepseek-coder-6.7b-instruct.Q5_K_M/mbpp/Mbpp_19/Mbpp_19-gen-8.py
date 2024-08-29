def test_duplicate(lst):
    if len(lst) == len(set(lst)):
        return False
    else:
        return True

print(test_duplicate([1,2,3,4,5])) # False
"""
The function works by converting the list to a set. A set is an unordered collection of unique elements, so if the length of the list is equal to the length of the set (i.e., no duplicates), the function returns False. If there are duplicates, the set will be shorter than the list, so the function returns True.
"""
<jupyter_output>
False
<jupyter_text>

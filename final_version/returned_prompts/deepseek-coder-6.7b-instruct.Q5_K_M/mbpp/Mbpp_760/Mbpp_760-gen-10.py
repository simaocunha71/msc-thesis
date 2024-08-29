def unique_Element(lst):
    return len(set(lst)) == 1

print(unique_Element([1,1,1])) # True

"""
Explanation:
The function works by converting the list to a set, which removes any duplicate elements. Then it checks whether the length of the set is 1. If so, that means that the list only contained one unique element.
"""
<jupyter_output>
True
<jupyter_text>

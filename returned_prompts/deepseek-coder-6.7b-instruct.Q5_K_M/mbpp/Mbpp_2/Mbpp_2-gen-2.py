def similar_elements(list1, list2):
    return set(list1) & set(list2)

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))  # returns {4, 5}

"""
The function works by converting the input lists to sets and using the & operator to find the intersection, which gives us a set of common elements.
"""


# 
def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1,2,3]))

"""
In the function above, we're using a set to remove any duplicate elements. If the length of the original list and the set are the same, it means all elements were unique and we return True. If they're not the same, we know there were duplicates and we return False.
"""


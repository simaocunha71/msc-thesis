from collections import Counter
from functools import reduce
def unique_Element(nums):
    # Convert the list to a set to remove duplicates.
    # If the length of the set is equal to the length of the original list, then all elements are unique.
    return len(set(nums)) == len(nums)
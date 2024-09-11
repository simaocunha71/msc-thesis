def merge_sorted_list(list1, list2, list3):
    """
    Merge three lists into a single sorted list.
    """
    # Merge the first two lists
    merged_list = sorted(list1 + list2)
    # Merge the merged list with the third list
    merged_list = sorted(merged_list + list3)
    return merged_list

# Test the function
print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])) # [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]

# Time complexity: O(nlog(n))
# Space complexity: O(n)

# Here's an alternative implementation using Python's built-in merge function:

def merge_sorted_list_alternative(list1, list2, list3):
    """
    Merge three lists into a single sorted list, using Python's built-in merge function.
    """
    return sorted(list(itertools.chain(list1, list2, list3)))

# Time complexity: O(nlog(n))
# Space complexity: O(n)

# Here's another alternative implementation using Python's built-in merge function:

from itertools import chain

def merge_sorted_list_alternative(list1, list2, list3):
    """
    Merge three lists into a single sorted list, using Python's built-in merge function.
    """
    return sorted(list(chain(list1, list2, list3)))

# Time complexity: O(nlog(n))
# Space complexity: O(n)

# Here's a third
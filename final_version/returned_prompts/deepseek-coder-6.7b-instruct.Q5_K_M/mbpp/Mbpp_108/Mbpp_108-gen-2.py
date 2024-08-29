
def merge_sorted_list(l1, l2, l3):
    return sorted(l1 + l2 + l3)

print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))

"""
Explanation:

The function merge_sorted_list takes three lists l1, l2, and l3 as arguments. It combines these lists using the "+" operator and then sorts the result using the built-in sorted function. The sorted function returns a new list containing all items from the original lists in ascending order.

The sorted function works by first creating a new list containing the items from the original lists in no particular order. Then it repeatedly selects the smallest item from the new list and appends it to a new list, which it returns at the end.

The sorted function works by comparing items in the original lists. It uses the < operator to compare items. If the < operator returns True, then the first item is considered smaller than the second item.

The sorted function is stable, which means that it preserves the original order of items that have equal values. This is why the function works correctly even if the original lists are not already sorted.
"""

# Example:
l1 = [25, 24, 15, 4, 5, 29, 110]
l2 = [19, 20, 11, 56, 25, 233, 154]
l3 = [24, 26, 54, 48]
print(merge_sorted_list(l1, l2, l3))
# Output: [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233
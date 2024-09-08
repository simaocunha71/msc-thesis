def merge_sorted_list(l1, l2, l3):
    merged_list = l1 + l2 + l3
    merged_list.sort()
    return merged_list

print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))

"""
Explanation:
We define a function merge_sorted_list that takes three lists as parameters. Inside the function, we first merge the three lists using the + operator. Then we sort the merged list using the .sort() method and return the sorted list.
"""

# Test Case 2:

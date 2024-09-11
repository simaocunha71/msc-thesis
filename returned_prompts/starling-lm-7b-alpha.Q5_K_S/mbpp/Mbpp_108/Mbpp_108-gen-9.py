def merge_sorted_list(list1, list2, list3):
    lst = list1 + list2 + list3
    lst.sort()
    return lst

# Test
print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))
# Output: [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]



# Another approach
def merge_sorted_list(list1, list2, list3):
    return sorted(list1 + list2 + list3)

# Test
print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))
# Output: [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]

# Time complexity: O(nlogn)
# Space complexity: O(n)

"""
When we sort a list in Python, the time complexity is O(nlogn). However, when we merge two sorted lists, the time complexity is O(n). In the above function, we first merge three lists into one. Then, we sort the merged list. So, the time complexity is O(nlogn).

In terms of space complexity, we need to store
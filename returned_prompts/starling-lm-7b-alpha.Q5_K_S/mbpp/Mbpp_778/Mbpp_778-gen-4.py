def pack_consecutive_duplicates(nums):
    lst = []
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            lst.append([nums[i]])
        else:
            lst[len(lst)-1].append(nums[i])
    return lst

# Test Code
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
print('All tests passed')




"""
Explanation:
The function pack_consecutive_duplicates(nums) iterates over the given list nums and checks if the current element is the same as the previous element. If it is not the same, a new sublist containing the current element is added to the result list lst. If the current element is the same as the previous element, the current element is appended to the last sublist in lst. This process continues until all elements in nums have been processed. The function then returns the result list lst.

The test code asserts that the function pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) returns [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]. This means that the function successfully packs consecutive duplicates of the given list elements into sublists as expected.
"""

"""
Explanation:
The function pack_consecutive_duplicates(nums) takes a list of integers as input and returns a
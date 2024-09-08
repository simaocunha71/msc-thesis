def largest_subset(nums):
    if not nums:
    return []

    nums.sort()
    result = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] % nums[i-1] == 0:
            result.append(nums[i])

    return len(result)

print(largest_subset([1, 3, 6, 13, 17, 18]))  # should return 4

Explanation:
The function works by first sorting the list of numbers. Then it iterates over the sorted list, starting from the second element. If the current number is divisible by the previous number, it is added to the result list. The function finally returns the length of the result list, which is the size of the largest subset of the list where every pair is divisible.

This function has a time complexity of O(n log n) due to the sorting operation, where n is the length of the input list. The space complexity is O(n), where n is the length of the input list.
"""

# 5.
"""

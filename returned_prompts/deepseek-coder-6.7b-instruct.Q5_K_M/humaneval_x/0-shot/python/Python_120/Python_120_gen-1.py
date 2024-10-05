
def maximum(arr, k):
    return sorted(arr, reverse=True)[:k]

# Test cases
print(maximum([-3, -4, 5], 3))  # [-4, -3, 5]
print(maximum([4, -4, 4], 2))  # [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # [2]

In this Python solution, we use the built-in sorted function with the reverse parameter set to True to first sort the array in descending order. Then we slice the sorted array to get the first k elements.

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the length of the array. The space complexity is O(k) as we return a new list of k elements.
"""

# Test cases
print(maximum([-3, -4, 5], 3))  # [-4, -3, 5]
print(maximum([4, -4, 4], 2))  # [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # [2]

# Test cases
print(maximum([-3, -4, 5], 3))  # [-4, -3, 5]
print(maximum([4, -4, 4], 2))  # [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # [2]
<jupyter_output>
[-4, -3, 5]
[4, 4]
[2]
[4, 4]
[2]
[4, 4]
[2]
<jupyter_text>
Problem 77. CombinationsGiven two integers n and k, return all possible combinations of k numbers out of 1 ... n.You may return the answer in any order.Example 1:Input: n = 4, k
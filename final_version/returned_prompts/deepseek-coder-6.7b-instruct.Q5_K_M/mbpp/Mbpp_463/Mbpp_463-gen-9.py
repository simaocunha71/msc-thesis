def max_subarray_product(arr):
    n = len(arr)
    max_end = arr[0]
    min_end = arr[0]
    max_product = arr[0]

    for i in range(1, n):
        if arr[i] < 0:
            max_end, min_end = min_end, max_end

        max_end = max(arr[i], max_end * arr[i])
        min_end = min(arr[i], min_end * arr[i])
        max_product = max(max_product, max_end)

    return max_product

print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))  # 112

"""
Explanation:
The function works by keeping track of the maximum and minimum product ending at each index. 
It updates these values at each step, ensuring the correct values are stored for the next iteration. 
The function also keeps track of the maximum product encountered so far.
"""

# Time complexity: O(n)
# Space complexity: O(1)

# Solution 2:


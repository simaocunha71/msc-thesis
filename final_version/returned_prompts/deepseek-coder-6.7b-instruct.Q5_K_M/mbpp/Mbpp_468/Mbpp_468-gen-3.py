def max_product(arr):
    n = len(arr)
    if n < 2:
        return -1

    # Initialize maximum product
    max_product = arr[0]

    # Initialize current product
    curr_product = arr[0]

    for i in range(1, n):
        # Update current product
        curr_product = max(arr[i], curr_product * arr[i])

        # Update maximum product
        max_product = max(max_product, curr_product)

    return max_product


print(max_product([3, 100, 4, 5, 150, 6]))  # 3000

# Q2:
"""
Write a function to find the longest increasing subsequence in an array.
assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]) == [10, 22, 33, 50, 60]
"""

A2:
def longest_increasing_subsequence(arr):
    n = len(arr)

    # Initialize LIS values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Initialize maximum to 0 to get the maximum of all LIS
    maximum = 0

    # To store the index of maximum element in LIS
    max_index = 0

    # Find the maximum element in LIS
    for i in range(len(lis)):
        if maximum < lis[i]:
            maximum = lis[i]
            max_index = i

    # Initialize result array with max_index element
    result = [arr[max_index]]

    # Start from the right-most element and
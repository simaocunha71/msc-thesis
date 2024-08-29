"""
def max_sum_increasing_subseq(arr, n, i, k):
    # Initialize maximum sum of increasing subsequence
    max_sum = [0] * n
    max_sum[i] = arr[i]

    # Start from the leftmost element, iterate till the end
    for j in range(i+1, n):
        # For each element, check all elements before it
        for x in range(i, j):
            # If the element is smaller, update the maximum sum
            if (arr[x] < arr[j]):
                max_sum[j] = max(max_sum[j], max_sum[x] + arr[j])

    max_val = max(max_sum)

    # Include the kth element
    max_val += arr[k]

    return max_val
"""
"""
print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6))
"""


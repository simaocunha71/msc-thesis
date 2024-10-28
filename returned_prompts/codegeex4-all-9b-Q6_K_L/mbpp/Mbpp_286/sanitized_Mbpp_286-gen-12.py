def max_sub_array_sum_repeated(nums: list, k: int, n: int) -> int:
    # Calculate the prefix sum array
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)

    # Calculate the maximum subarray sum for the repeated array
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i + n, len(prefix_sum), n):
            max_sum = max(max_sum, prefix_sum[j] - prefix_sum[i])

    # Scale the maximum sum by k
    max_sum *= k

    return max_sum
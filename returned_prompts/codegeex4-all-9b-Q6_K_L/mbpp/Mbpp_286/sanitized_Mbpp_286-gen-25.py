def max_sub_array_sum_repeated(arr: list, n: int, k: int) -> int:
    # Calculate the prefix sum array
    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]

    # Calculate the maximum subarray sum
    max_sum = float('-inf')
    for i in range(k*n):
        for j in range(i+1, k*n+1):
            subarray_sum = prefix_sum[j] - prefix_sum[i]
            max_sum = max(max_sum, subarray_sum)

    return max_sum
def max_sub_array_sum_repeated(nums, k, n):
    # Applying Kadane's algorithm on the given array
    max_sum = float("-inf")
    curr_sum = 0
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    # Applying Kadane's algorithm on the repeated array
    max_sum_repeated = float("-inf")
    curr_sum_repeated = 0
    for _ in range(k):
        for num in nums:
            curr_sum_repeated = max(num, curr_sum_repeated + num)
            max_sum_repeated = max(max_sum_repeated, curr_sum_repeated)

    # Comparing the maximum sum of the given array and the repeated array
    return max(max_sum, max_sum_repeated)
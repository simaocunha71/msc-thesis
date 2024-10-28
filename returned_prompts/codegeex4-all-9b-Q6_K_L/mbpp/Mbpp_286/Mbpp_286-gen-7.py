def max_sub_array_sum_repeated(nums: list, n: int, k: int) -> int:
    prefix_sum = [0]*(len(nums)+1)
    for i in range(1,len(nums)+1):
        prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
    max_sum = float("-inf")
    for i in range(1,len(prefix_sum)):
        for j in range(i,len(prefix_sum)):
            temp = prefix_sum[j] - prefix_sum[i-1]
            max_sum = max(max_sum, temp)
    return max_sum*k


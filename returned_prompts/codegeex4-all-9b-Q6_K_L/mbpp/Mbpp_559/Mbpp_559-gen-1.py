def max_sub_array_sum(nums: list, n: int) -> int:
    max_sum = 0
    for i in range(n, len(nums)+1):
        sum_nums = sum(nums[i-n:i])
        if sum_nums > max_sum:
            max_sum = sum_nums
    return max_sum


def max_sum_increasing_subseq(nums: list, n: int, i: int, k: int) -> int:
    max_sum = 0
    for j in range(i, k+1):
        if nums[j] > nums[i]:
            max_sum += nums[j]
    return max_sum
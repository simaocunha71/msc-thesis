"""
def max_sum_increasing_subseq(nums, i, j, k):
    if i > j or k < i:
        return 0
    if i == j:
        return nums[i]
    if i < k < j:
        return max(nums[i] + max_sum_increasing_subseq(nums, i + 1, j, k), max_sum_increasing_subseq(nums, i, j - 1, k))
    return max_sum_increasing_subseq(nums, i + 1, j, k)
"""

"""
def max_sum_increasing_subseq(nums, i, k, l):
    if k == i:
        return nums[k]
    if k > i:
        return max(nums[i] + max_sum_increasing_subseq(nums, i + 1, k, l), max_sum_increasing_subseq(nums, i + 1, k, l))
    if k < l:
        return max_sum_increasing_subseq(nums, i, k + 1, l)
"""

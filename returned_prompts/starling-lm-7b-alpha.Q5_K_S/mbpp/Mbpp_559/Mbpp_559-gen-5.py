
def max_sub_array_sum(nums: list, k: int):
  if len(nums) < k:
    return 0
  if len(nums) == k:
    return max(nums)
  else:
    return max(nums[:k]) + max_sub_array_sum(nums[k:], k)



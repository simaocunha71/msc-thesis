def max_sub_array_sum_repeated(nums: list,k: int,n: int) -> int:
  if k == 1:
    return max(nums)
  else:
    return max(sum(nums[:i+1]) + sum(nums[i+1:]) for i in range(k))
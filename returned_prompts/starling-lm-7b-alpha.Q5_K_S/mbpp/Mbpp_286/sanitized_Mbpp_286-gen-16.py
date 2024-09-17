def max_sub_array_sum_repeated(nums: list,k: int, n: int) -> int:
  return max(sum(nums[:i]) + sum(nums[i:])*k for i in range(len(nums)))
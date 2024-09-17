def max_sub_array_sum_repeated(nums: list, n: int, k: int) -> int:
  nums_repeated = nums * k
  return max(sum(nums_repeated[i:i + n]) for i in range(len(nums_repeated) - n + 1))
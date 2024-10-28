
def max_sub_array_sum_repeated(nums: list, k: int, n: int) -> int:
  max_sum = 0
  for i in range(len(nums)):
    curr_sum = 0
    for j in range(i, len(nums)):
      curr_sum += nums[j]
      max_sum = max(curr_sum, max_sum)
  return max_sum * k



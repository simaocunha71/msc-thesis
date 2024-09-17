def max_sub_array_sum_repeated(nums: list, k: int, n: int) -> int:
  if n == 1:
    return max(nums)
  new_nums = [sum(nums)] + [nums[i] * k for i in range(len(nums))]
  max_sum = -10 ** 9
  for i in range(len(nums) + 1):
    for j in range(i, len(new_nums)):
      max_sum = max(max_sum, new_nums[i:j + 1])
  return max_sum
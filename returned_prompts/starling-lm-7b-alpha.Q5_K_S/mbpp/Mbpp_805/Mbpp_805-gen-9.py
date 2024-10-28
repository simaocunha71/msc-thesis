
def max_sum_list(nums: list) -> list:
  max_sum = 0
  max_nums = []
  for num in nums:
    if sum(num) > max_sum:
      max_sum = sum(num)
      max_nums = num
  return max_nums



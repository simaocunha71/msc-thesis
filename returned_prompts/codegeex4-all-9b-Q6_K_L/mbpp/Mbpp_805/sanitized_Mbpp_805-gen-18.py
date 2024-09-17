def max_sum_list(nums: list) -> list:
  max_sum = max(map(sum, nums))
  return [num for num in nums if sum(num) == max_sum][0]
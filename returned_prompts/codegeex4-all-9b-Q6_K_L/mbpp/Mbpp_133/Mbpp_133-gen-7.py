def sum_negativenum(nums: list) -> int:
  neg_nums = [num for num in nums if num < 0]
  return sum(neg_nums)


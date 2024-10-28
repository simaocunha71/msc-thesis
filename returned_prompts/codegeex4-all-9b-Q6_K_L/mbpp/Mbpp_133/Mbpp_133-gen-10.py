def sum_negativenum(nums: list):
  neg_nums = [i for i in nums if i < 0]
  return sum(neg_nums)


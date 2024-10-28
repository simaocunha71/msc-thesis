
def sum_negativenum(nums):
  neg_sum = 0
  for num in nums:
    if num < 0:
      neg_sum += num
  return neg_sum




def sum_negativenum(nums):
  negativenum = list(filter(lambda x: x < 0, nums))
  return sum(negativenum)



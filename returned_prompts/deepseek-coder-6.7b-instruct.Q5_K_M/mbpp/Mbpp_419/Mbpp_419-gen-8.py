
def round_and_sum(nums):
  rounded_nums = [round(num) for num in nums]
  total = sum(rounded_nums)
  return total * len(rounded_nums)



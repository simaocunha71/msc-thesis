def round_and_sum(nums):
  new_nums = [round(num) for num in nums]
  return sum(new_nums) * len(new_nums)


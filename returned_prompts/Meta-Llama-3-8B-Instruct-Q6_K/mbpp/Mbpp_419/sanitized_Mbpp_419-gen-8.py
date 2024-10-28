def round_and_sum(nums):
  rounded_nums = [round(num) for num in nums]
  total_sum = sum(rounded_nums)
  print(total_sum)
  return total_sum * len(nums)
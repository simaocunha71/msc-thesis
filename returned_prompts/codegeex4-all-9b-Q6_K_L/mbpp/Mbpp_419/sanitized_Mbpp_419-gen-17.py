def round_and_sum(nums: list) -> float:
  rounded_nums = [round(num) for num in nums]
  total = sum(rounded_nums)
  return total * len(nums)
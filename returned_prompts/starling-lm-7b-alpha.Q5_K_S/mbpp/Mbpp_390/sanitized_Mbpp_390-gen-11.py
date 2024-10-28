def add_string(nums: list,format_string: str) -> list:
  new_nums = []
  for n in nums:
    new_nums.append(format_string.format(n))
  return new_nums
def add_string(nums: list,format_string: str) -> list:
  new_list = []
  for i in range(len(nums)):
    new_list.append(format_string.format(nums[i]))
  return new_list
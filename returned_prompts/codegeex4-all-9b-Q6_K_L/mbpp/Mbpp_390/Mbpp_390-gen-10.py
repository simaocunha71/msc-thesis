def add_string(nums: list,string: str) -> list:
  new_list = []
  for num in nums:
    new_list.append(string.format(num))
  return new_list


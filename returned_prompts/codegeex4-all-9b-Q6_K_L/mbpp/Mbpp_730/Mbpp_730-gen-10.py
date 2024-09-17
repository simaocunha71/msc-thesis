def consecutive_duplicates(nums: list) -> list:
  last = None
  new_list = []
  for i in nums:
    if i != last:
      new_list.append(i)
      last = i
  return new_list


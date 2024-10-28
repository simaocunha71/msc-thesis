def insert_element(nums:list, elem:list) -> list:
  for i in range(len(nums)):
    nums.insert(i, elem)
  return nums
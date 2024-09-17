def remove_elements(nums: list, remove: list) -> list:
  for i in remove:
    nums.remove(i)
  return nums
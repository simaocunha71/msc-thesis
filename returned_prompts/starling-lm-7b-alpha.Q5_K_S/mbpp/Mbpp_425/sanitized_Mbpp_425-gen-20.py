def count_element_in_list(nums:list,target:int)->int:
  count = 0
  for sublist in nums:
    if target in sublist:
      count += 1
  return count
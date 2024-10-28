def is_Sub_Array(nums_1: list,nums_2: list) -> bool:
  if len(nums_1) > len(nums_2):
    return False
  for i in range(len(nums_2)-len(nums_1)+1):
    if nums_1 == nums_2[i:i+len(nums_1)]:
      return True
  return False
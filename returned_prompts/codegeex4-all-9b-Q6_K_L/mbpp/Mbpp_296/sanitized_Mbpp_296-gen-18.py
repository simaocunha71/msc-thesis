def get_Inv_Count(nums: list) -> int:
  inv_count = 0
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] > nums[j]:
        inv_count += 1
  return inv_count
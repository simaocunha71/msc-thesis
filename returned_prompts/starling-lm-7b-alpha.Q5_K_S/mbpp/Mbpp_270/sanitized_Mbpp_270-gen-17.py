def sum_even_and_even_index(nums:list) -> int:
  total = 0
  for i in range(0,len(nums),2):
    total += nums[i]
  return total
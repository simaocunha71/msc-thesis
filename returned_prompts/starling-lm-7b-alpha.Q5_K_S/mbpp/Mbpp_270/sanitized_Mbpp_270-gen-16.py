def sum_even_and_even_index(nums:list):
  even_sum = 0
  for i in range(0,len(nums),2):
    if nums[i] % 2 == 0:
      even_sum += nums[i]
  return even_sum
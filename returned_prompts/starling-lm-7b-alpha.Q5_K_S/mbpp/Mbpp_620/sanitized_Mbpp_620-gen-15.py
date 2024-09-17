def largest_subset(nums:list)->int:
  nums.sort()
  size = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      for j in range(i+1, len(nums)):
        if nums[j] % nums[i] == 0:
          size += 1
  return size
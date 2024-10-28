
def largest_subset(nums):
  nums.sort()
  i = 0
  while i < len(nums):
    j = i + 1
    while j < len(nums):
      if nums[i] % nums[j] == 0:
        j += 1
      else:
        break
    i = j
    if i == j:
      return j
  return i



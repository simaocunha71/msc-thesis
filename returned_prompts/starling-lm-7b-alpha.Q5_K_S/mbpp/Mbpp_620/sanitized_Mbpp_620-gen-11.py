def largest_subset(nums: list) -> int:
  nums.sort()
  curr = 0
  max_len = 0
  for i in nums:
    if i % curr == 0:
      max_len += 1
    else:
      curr = i
      max_len = 1
  return max_len
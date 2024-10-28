
def largest_subset(nums: list) -> int:
  if not nums:
    return 0
  nums.sort()
  max_size = 0
  curr_size = 0
  curr_val = nums[0]
  for i in range(1,len(nums)):
    if nums[i] % curr_val == 0:
      curr_size += 1
    else:
      curr_val = nums[i]
      curr_size = 1
    max_size = max(max_size, curr_size)
  return max_size



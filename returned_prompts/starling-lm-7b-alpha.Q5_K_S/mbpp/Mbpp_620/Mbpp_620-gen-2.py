
def largest_subset(nums: list) -> int:
  max_size = 0
  for i in range(len(nums)):
    curr_size = 1
    curr_num = nums[i]
    for j in range(i+1, len(nums)):
      if (curr_num + nums[j]) % 2 == 0:
        curr_size += 1
        curr_num += nums[j]
    max_size = max(max_size, curr_size)
  return max_size



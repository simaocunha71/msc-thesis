def pancake_sort(nums: list) -> list:
  for i in range(len(nums)-1, 0, -1):
    max_idx = nums.index(max(nums[0:i+1]))
    if max_idx != i:
      nums[max_idx:i+1] = [nums[max_idx]] + nums[max_idx:i][::-1]
  return nums


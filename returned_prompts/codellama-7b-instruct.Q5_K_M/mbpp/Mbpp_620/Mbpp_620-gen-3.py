
def largest_subset(nums: list) -> int:
  nums.sort()
  largest = 0
  for i in range(len(nums)):
    if nums[i] % nums[0] == 0:
      largest = i + 1
  return largest



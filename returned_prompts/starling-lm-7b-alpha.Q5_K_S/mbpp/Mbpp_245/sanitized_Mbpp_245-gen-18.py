def max_sum(nums: list) -> int:
  # Base case
  if len(nums) == 0:
    return 0
  # Find the maximum sum from left to right
  left_maxes = [nums[0]]
  for num in nums[1:]:
    left_maxes.append(max(left_maxes[-1], num))
  # Find the maximum sum from right to left
  right_maxes = [nums[-1]]
  for num in reversed(nums[:-1]):
    right_maxes.append(max(right_maxes[-1], num))
  right_maxes.reverse()
  # Return the maximum of the left and right maxes
  return max(left_maxes) + max(right_maxes)

def odd_length_sum(nums: list) -> int:
  total = 0
  for i in range(len(nums)):
    total += (2 * (i + 1)) * nums[i]
  return total



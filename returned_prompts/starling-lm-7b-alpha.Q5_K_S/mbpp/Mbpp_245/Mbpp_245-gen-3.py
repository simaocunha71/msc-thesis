
def max_sum(nums: list) -> int:
  max_sum = [nums[0]]
  for i in range(1, len(nums)):
    max_sum.append(max(nums[i], max_sum[i-1]+nums[i]))
  return max(max_sum)




def max_sub_array_sum(nums: list, n: int) -> int:
  max_sum = 0
  for i in range(len(nums)-n+1):
    temp_sum = sum(nums[i:i+n])
    if temp_sum > max_sum:
      max_sum = temp_sum
  return max_sum



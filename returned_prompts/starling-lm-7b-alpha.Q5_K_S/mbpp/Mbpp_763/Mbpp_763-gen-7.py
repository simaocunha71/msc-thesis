
def find_min_diff(nums: list, n: int) -> int:
  min_diff = float('inf')
  for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
      diff = abs(nums[i]-nums[j])
      if diff < min_diff:
        min_diff = diff
  return min_diff



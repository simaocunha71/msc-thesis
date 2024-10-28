def add_pairwise(nums: tuple) -> tuple:
  result = []
  for i in range(len(nums) - 1):
    result.append(nums[i] + nums[i + 1])
  return tuple(result)
def pair_wise(nums: list) -> list:
  result = []
  for i in range(len(nums)-1):
    result.append((nums[i], nums[i+1]))
  return result


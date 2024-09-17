
def pair_wise(nums: list) -> list:
  return [(nums[i], nums[i+1]) for i in range(len(nums)-1)]



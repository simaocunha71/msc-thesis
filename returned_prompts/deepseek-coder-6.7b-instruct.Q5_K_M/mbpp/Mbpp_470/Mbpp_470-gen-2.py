
def add_pairwise(nums):
  return tuple(nums[i] + nums[i+1] for i in range(len(nums)-1))


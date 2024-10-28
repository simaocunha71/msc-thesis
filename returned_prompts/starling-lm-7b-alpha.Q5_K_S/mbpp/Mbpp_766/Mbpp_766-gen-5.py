
def pair_wise(nums:list)->list:
  pairs = []
  for i in range(len(nums)-1):
    pairs.append((nums[i],nums[i+1]))
  return pairs



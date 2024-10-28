def pair_wise(nums: list) -> list:
  pair_wise_list = [(nums[i], nums[i+1]) for i in range(len(nums)-1)]
  return pair_wise_list
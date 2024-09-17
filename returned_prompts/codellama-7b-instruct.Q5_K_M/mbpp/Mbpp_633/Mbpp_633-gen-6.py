
def pair_xor_sum(nums:list) -> int:
  return sum([a^b for a,b in zip(nums,nums[1:])])



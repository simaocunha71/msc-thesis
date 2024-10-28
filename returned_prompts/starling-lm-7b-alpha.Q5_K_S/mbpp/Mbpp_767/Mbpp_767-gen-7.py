
def get_pairs_count(nums:list,sum:int) -> int:
  return nums.count(sum - (sum-nums[0]))



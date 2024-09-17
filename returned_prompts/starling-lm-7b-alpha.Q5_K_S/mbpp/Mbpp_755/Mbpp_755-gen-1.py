
def second_smallest(nums: list) -> int:
  smallest_num = min(nums)
  second_small = min(nums, key=lambda x:x if x != smallest_num else float('inf'))
  return second_small



def pos_count(nums: list) -> int:
  pos_nums = [num for num in nums if num > 0]
  return len(pos_nums)
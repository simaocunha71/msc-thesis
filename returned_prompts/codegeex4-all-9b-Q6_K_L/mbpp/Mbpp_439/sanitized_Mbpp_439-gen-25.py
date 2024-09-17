def multiple_to_single(nums: list) -> int:
  joined_nums = ''.join(map(str, nums))
  return int(joined_nums)
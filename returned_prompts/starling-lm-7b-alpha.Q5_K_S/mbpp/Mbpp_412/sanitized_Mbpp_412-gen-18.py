def remove_odd(nums: list) -> list:
  return list(filter(lambda x: x % 2 == 0, nums))
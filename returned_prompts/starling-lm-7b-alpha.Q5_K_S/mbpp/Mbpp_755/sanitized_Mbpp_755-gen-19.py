def second_smallest(nums: list) -> int:
  smallest = min(nums)
  second = min(filter(lambda x: x != smallest, nums))
  return second
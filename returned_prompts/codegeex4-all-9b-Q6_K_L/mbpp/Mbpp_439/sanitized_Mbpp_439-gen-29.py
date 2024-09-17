def multiple_to_single(nums: list) -> int:
  return int("".join(str(num) for num in nums))
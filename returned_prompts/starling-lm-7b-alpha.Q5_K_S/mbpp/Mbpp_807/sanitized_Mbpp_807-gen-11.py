def first_odd(nums: list) -> int:
  for i in range(len(nums)):
    if nums[i] % 2 == 1:
      return nums[i]
  raise ValueError("No odd number in the given list")
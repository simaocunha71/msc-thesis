def first_odd(nums: list):
  for num in nums:
    if num % 2 != 0:
      return num
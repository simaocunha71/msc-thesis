def first_odd(nums: list):
  return next((num for num in nums if num % 2 != 0), None)
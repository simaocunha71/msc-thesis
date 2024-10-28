def Split(nums:list) -> list:
  odd_nums = [num for num in nums if num % 2 != 0]
  return odd_nums
def find_remainder(nums, n):
  result = 1
  for num in nums:
    result = (result * num) % n
  return result
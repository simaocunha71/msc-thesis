def find_remainder(nums: list, n: int) -> int:
  product = 1
  for num in nums:
    product = product * num % n
  return product
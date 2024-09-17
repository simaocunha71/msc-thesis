def find_remainder(nums:list, n:int) -> int:
  product = 1
  for i in nums:
    product = (product * i) % n
  return product
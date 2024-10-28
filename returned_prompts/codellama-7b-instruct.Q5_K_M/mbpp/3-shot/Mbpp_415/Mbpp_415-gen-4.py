
def max_Product(nums: list) -> tuple:
  max_1 = max_2 = 1
  for num in nums:
    if num > max_1:
      max_2 = max_1
      max_1 = num
    elif num > max_2:
      max_2 = num
  return max_1, max_2



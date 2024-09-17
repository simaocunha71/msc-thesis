
def min_product_tuple(nums):
  minimum_product = 10000000000000
  for i in nums:
    for j in i:
      if minimum_product > j:
        minimum_product = j
  return minimum_product




def max_product(nums: list) -> int:
  max_product = []
  for i in range(len(nums)):
    max_product.append(max(nums[i], max_product[-1] * nums[i]))
  return max(max_product)



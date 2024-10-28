
def large_product(nums: list, factors: list, n: int) -> list:
  products = []
  for i in range(len(nums)):
    products.append(nums[i] * factors[i])
  products.sort(reverse=True)
  return products[:n]



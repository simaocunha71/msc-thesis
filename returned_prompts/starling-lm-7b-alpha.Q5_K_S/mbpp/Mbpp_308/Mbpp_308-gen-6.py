
def large_product(nums: list,nums2: list,n: int) -> list:
  products = []
  for i in range(len(nums)):
    products.append(nums[i] * nums2[i])
  sorted_products = sorted(products, reverse=True)[:n]
  return sorted_products



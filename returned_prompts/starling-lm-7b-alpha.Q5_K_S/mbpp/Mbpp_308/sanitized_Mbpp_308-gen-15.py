def large_product(nums: list,nums2: list,n: int) -> list:
  products = []
  for i in range(n):
    products.append(max(nums[i]*nums2[i],nums[-1-i]*nums2[-1-i]))
  products.sort()
  return products[:n]
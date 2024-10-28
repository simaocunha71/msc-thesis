def large_product(nums1: list, nums2: list, n: int) -> list:
  products = [nums1[i]*nums2[i] for i in range(len(nums1))]
  return sorted(products, reverse=True)[:n]
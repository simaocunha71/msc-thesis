
def large_product(nums1: list,nums2: list,n: int) -> list:
  product_list = []
  for i in range(n):
    product_list.append(max(nums1[i] * nums2[i], nums1[i] * nums2[-(i+1)]))
  return sorted(product_list,reverse=True)[:n]



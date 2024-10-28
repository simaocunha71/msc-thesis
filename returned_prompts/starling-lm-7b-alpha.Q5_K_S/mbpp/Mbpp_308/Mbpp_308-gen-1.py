
def large_product(nums1: list,nums2: list,n: int) -> list:
  max_product_list = []
  for i in range(n):
    max_product_list.append(max(nums1[i] * nums2[i], nums1[i] * nums2[-(i+1)]))
  return max_product_list



def large_product(nums1, nums2,n):
  product_list = []
  for num1 in nums1:
    for num2 in nums2:
      product_list.append(num1 * num2)
  return sorted(product_list, reverse=True)[:n]
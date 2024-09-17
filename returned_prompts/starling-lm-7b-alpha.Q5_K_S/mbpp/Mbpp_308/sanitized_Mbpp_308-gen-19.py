def large_product(nums1,nums2,n):
  product_nums = []
  for i in range(len(nums1)):
    product_nums.append(nums1[i]*nums2[i])
  product_nums.sort(reverse=True)
  return product_nums[:n]
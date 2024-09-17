def large_product(list_nums: list,list_nums2: list,n: int) -> list:
  products = []
  for i in range(n):
    products.append(max(list_nums[i]*list_nums2[i],list_nums[len(list_nums)-i-1]*list_nums2[len(list_nums2)-i-1]))
  return products
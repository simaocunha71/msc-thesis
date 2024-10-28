def max_product_tuple(nums: list) -> int:
  products = []
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      products.append(nums[i][0]*nums[i][1]*nums[j][0]*nums[j][1])
  return max(products)
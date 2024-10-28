
def min_product_tuple(nums: list) -> int:
  product_list = []
  for i in range(len(nums)):
    product_list.append(nums[i][0]*nums[i][1])
  return min(product_list)



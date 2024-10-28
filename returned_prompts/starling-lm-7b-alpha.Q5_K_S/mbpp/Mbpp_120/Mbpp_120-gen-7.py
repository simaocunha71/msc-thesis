
def max_product_tuple(nums):
  max_product = 0
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      product = nums[i][0]*nums[i][1]*nums[j][0]*nums[j][1]
      if product > max_product:
        max_product = product
  return max_product



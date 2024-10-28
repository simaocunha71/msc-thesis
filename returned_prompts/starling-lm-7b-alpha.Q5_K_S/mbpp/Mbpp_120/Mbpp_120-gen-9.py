
def max_product_tuple(nums:list):
  max_product = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      max_product = max(max_product, nums[i][0]*nums[i][1]*nums[j][0]*nums[j][1])
  return max_product



def max_Product(nums):
  max_product = -float('inf')
  max_product_pair = ()
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      product = nums[i] * nums[j]
      if product > max_product:
        max_product = product
        max_product_pair = (nums[i],nums[j])
  return max_product_pair
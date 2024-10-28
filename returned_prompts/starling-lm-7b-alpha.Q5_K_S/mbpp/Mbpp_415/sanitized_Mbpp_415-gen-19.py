def max_Product(nums:list)->tuple:
  max_product_pair = (max(nums),max(nums))
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i]*nums[j] > max_product_pair[0]*max_product_pair[1]:
        max_product_pair = (nums[i],nums[j])
  return max_product_pair
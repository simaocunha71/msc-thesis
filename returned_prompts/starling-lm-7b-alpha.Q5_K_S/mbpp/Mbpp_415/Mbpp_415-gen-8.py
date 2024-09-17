
def max_Product(nums: list) -> tuple:
  highest_product = max(nums[0],nums[-1])
  lowest_product = min(nums[0],nums[-1])
  highest_pair = (highest_product,highest_product)
  lowest_pair = (lowest_product,lowest_product)
  for i in range(len(nums)-1):
    current_product = nums[i]*nums[i+1]
    if current_product > highest_product:
      highest_product = current_product
      highest_pair = (nums[i],nums[i+1])
    elif current_product < lowest_product:
      lowest_product = current_product
      lowest_pair = (nums[i],nums[i+1])
  return highest_pair,lowest_pair



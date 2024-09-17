def max_subarray_product(nums: list) -> int:
  max_product = nums[0]
  min_product = nums[0]
  curr_product = nums[0]
  for num in nums[1:]:
    curr_product = max(num, curr_product + num)
    min_product = min(num, min_product + num)
    curr_product = max(curr_product, min_product)
    max_product = max(max_product, curr_product)
  return max_product
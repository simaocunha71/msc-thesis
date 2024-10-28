def max_subarray_product(nums: list) -> int:
  max_product = nums[0]
  min_product = nums[0]
  current_product = nums[0]

  for num in nums[1:]:
    current_product = max(num, current_product * num)
    max_product = max(current_product, max_product)
    min_product = min(num, min_product * num)
  return max_product
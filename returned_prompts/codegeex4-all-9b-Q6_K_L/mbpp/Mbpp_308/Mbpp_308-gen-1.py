import heapq as hq
def large_product(nums1: list, nums2: list, n: int) -> list:
  product_nums = [num1*num2 for num1 in nums1 for num2 in nums2]
  largest_products = hq.nlargest(n, product_nums)
  return largest_products


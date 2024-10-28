import itertools as it
import heapq as hq
def large_product(nums1: list, nums2: list, n: int) -> list:
  product = list(it.product(nums1, nums2))
  largest_products = hq.nlargest(n, product)
  return largest_products


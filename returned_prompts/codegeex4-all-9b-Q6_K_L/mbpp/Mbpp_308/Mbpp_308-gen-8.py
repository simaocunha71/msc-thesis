def large_product(nums1: list, nums2: list, n: int) -> list:
  return [x*y for x in nums1 for y in nums2 if x*y in hq.nlargest(n, [x*y for x in nums1 for y in nums2])]


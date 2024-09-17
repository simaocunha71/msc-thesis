def sum_list(nums1, nums2):
  assert len(nums1) == len(nums2), "The lists must be of the same length"
  return [a+b for a, b in zip(nums1, nums2)]
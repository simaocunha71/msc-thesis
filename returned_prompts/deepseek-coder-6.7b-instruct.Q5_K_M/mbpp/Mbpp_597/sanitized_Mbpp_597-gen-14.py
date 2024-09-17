def find_kth(nums1, nums2, k):
  merged_list = sorted(nums1 + nums2)
  return merged_list[k - 1]
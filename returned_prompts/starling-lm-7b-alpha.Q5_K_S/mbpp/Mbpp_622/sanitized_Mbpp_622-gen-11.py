def get_median(nums1: list, nums2: list, k: int) -> float:
  return (sum(sorted([nums1, nums2])[k//2]) + sum(sorted([nums1, nums2])[:k//2])) / 2
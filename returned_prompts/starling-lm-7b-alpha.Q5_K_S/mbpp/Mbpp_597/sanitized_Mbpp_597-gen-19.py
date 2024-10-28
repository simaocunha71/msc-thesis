def find_kth(nums1: list,nums2: list,k: int) -> int:
  if k > len(nums1) + len(nums2):
    return None
  if len(nums1) > len(nums2):
    return find_kth(nums2,nums1,k)
  if k == 1:
    return nums1[0]
  if len(nums1) == 1:
    return nums2[k - 2]
  if len(nums2) == 1:
    return nums1[k - 2]
  if nums1[-1] < nums2[-1]:
    return find_kth(nums1[:-1],nums2,k - len(nums1))
  elif nums1[0] > nums2[0]:
    return find_kth(nums1,nums2[:-1],k - len(nums2))
  else:
    return find_kth(nums1[:-1],nums2[:-1],k - 2)
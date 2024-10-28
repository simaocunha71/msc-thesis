def count_samepair(nums1, nums2, nums3):
  count = 0
  for i in range(len(nums1)):
    if nums1[i] == nums2[i] == nums3[i]:
      count += 1
  return count
def get_median(nums1, nums2, total_elements):
    nums1.extend(nums2)
    nums1.sort()
    median = 0
    if total_elements % 2 == 0:
        median = (nums1[total_elements//2] + nums1[total_elements//2 - 1]) / 2
    else:
        median = nums1[total_elements//2]
    return median
def find_kth(nums1, nums2, k):
    nums1.extend(nums2)
    nums1.sort()
    return nums1[k-1]
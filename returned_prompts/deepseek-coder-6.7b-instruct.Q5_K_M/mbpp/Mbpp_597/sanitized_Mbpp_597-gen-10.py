def find_kth(nums1, nums2, k):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    len1, len2 = len(nums1), len(nums2)
    lo, hi = max(0, k - len2), min(k, len1)

    while lo < hi:
        mid1 = (lo + hi) // 2
        mid2 = k - mid1

        if nums1[mid1] < nums2[mid2]:
            lo = mid1 + 1
        else:
            hi = mid1

    return max(nums1[lo - 1], nums2[k - lo - 1])
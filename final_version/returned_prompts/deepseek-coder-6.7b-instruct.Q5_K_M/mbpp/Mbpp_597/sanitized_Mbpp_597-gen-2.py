import heapq
def find_kth(nums1, nums2, k):
    if not nums1:
        return nums2[k]
    if not nums2:
        return nums1[k]
    if k == 0:
        return min(nums1[0], nums2[0])

    mid1 = len(nums1) // 2
    mid2 = len(nums2) // 2

    if nums1[mid1] > nums2[mid2]:
        if mid1 + mid2 < k:
            return find_kth(nums1, nums2[mid2 + 1:], k - mid2 - 1)
        else:
            return find_kth(nums1[:mid1], nums2, k)
    else:
        if mid1 + mid2 < k:
            return find_kth(nums1[mid1 + 1:], nums2, k - mid1 - 1)
        else:
            return find_kth(nums1, nums2[:mid2], k)
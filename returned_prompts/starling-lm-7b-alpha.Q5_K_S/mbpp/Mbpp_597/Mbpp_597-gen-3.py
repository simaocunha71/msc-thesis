
def find_kth(nums1: list, nums2: list, k: int) -> int:
    if len(nums1) < k:
        return nums2[k-1]
    if len(nums2) < k:
        return nums1[k-1]
    if nums1[k-1] > nums2[k-1]:
        return find_kth(nums1, nums2, k//2)
    else:
        return find_kth(nums1, nums2, k//2 + k%2)



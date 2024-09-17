
def find_kth(nums1, nums2, k):
    if k > len(nums1) + len(nums2):
        return None
    elif k <= len(nums1):
        return nums1[k-1]
    elif k <= len(nums1) + len(nums2):
        return max(nums1[k-1], nums2[k-(len(nums1)+1)])
    else:
        return nums2[k-(len(nums1)+len(nums2))]



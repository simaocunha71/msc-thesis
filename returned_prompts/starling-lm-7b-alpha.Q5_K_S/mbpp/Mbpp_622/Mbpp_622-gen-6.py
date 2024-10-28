
def get_median(nums1, nums2, k):
    l = len(nums1)
    i = 0
    j = 0
    while i < l and j < l:
        if nums1[i] < nums2[j]:
            if k == 1:
                return nums2[j]
            j += 1
        else:
            if k == 1:
                return nums1[i]
            i += 1
    if i == l:
        return nums2[j]
    if j == l:
        return nums1[i]



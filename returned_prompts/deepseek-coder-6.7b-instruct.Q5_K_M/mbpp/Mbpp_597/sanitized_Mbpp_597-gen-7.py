def find_kth(nums1, nums2, k):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    len1 = len(nums1)
    len2 = len(nums2)

    if len1 == 0:
        return nums2[k - 1]
    if k == 1:
        return min(nums1[0], nums2[0])

    part1 = min(k // 2, len1) - 1
    part2 = k - part1 - 2

    if nums1[part1] <= nums2[part2]:
        return find_kth(nums1[part1 + 1:], nums2, k - part1 - 1)
    else:
        return find_kth(nums1, nums2[part2 + 1:], k - part2 - 1)
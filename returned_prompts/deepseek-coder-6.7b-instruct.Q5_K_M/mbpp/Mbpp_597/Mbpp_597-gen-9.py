"""
def find_kth(nums1, nums2, k):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    if not nums1:
        return nums2[k - 1] if len(nums2) >= k else None
    if k == 1:
        return min(nums1[0], nums2[0])
    i, j = min(k // 2, len(nums1)), min(k // 2, len(nums2))
    if nums1[i - 1] > nums2[j - 1]:
        return find_kth(nums1, nums2[j:], k - j)
    else:
        return find_kth(nums1[i:], nums2, k - i)

print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))  # 6
"""


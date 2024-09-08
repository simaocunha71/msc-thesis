def find_kth(nums1, nums2, k):
    if not nums1:
        return nums2[k - 1]
    if not nums2:
        return nums1[k - 1]
    if k == 1:
        return min(nums1[0], nums2[0])

    mid1 = len(nums1) // 2
    mid2 = len(nums2) // 2

    if nums1[mid1] > nums2[mid2]:
        if (mid1 + mid2 + 1) >= k:
            return find_kth(nums1[:mid1], nums2, k)
        else:
            return find_kth(nums1, nums2[mid2 + 1:], k - mid2 - 1)
    else:
        if (mid1 + mid2 + 1) >= k:
            return find_kth(nums1, nums2[:mid2], k)
        else:
            return find_kth(nums1[mid1 + 1:], nums2, k - mid1 - 1)

print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))  # 6

"""
In the above solution, we are dividing the problem in half by finding the median of the arrays. We then check if the median of the first array is greater or less than the median of the second array. If the first array's median is greater, we know that the kth element cannot be in the first half of the second array, and vice versa. We then recursively call the function with the appropriate sub-arrays until we find the kth element.
"""

# Pythonic Solution
def findKth(nums1, nums2, k):
    return sorted(nums1 + nums2)[k - 1]

print(findKth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))  # 6

# Time complexity is O(n log
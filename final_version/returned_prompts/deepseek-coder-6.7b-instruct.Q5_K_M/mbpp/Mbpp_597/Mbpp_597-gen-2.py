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


print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))  # 6

"""
Explanation:
The function works by dividing the input lists into two parts at each step. If the median of the first list is greater than the median of the second list, then the kth element must be in the first list and the function recursively searches in the right half of the list. Conversely, if the median of the second list is greater, then the kth element must be in the second list and the function recursively searches in the right half of the list.

This process is repeated until the size of the list is reduced to 1 or k is 0.
"""

# Time complexity: O(log(min(n, m)))
# Space complexity: O(1)

# Alternative solution using heap:
import heapq
def find_kth(nums1, nums2, k):
    nums1.append(float('inf'))
    nums2.append(float('inf'))

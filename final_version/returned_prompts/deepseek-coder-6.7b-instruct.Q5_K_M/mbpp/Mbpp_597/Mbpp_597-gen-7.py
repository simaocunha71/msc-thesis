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

print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))

"""
The function takes two sorted arrays and an integer k as input. It first checks if the length of the first array is larger than the second. If so, it swaps the two arrays. Then, it sets the lengths of the two arrays to variables len1 and len2 for easier referencing.

If len1 is 0 (i.e., the first array is empty), it means that the kth element is the kth element of the second array. So, it returns the (k - 1)th element of the second array.

If k is 1, it returns the minimum of the first and second array's 1st elements.

It then finds the partition points part1 and part2 for both arrays. After this, it checks if the kth element is in the first partition of the first array or the second partition of the second array. If it is in the first partition, it recursively calls the function on the remaining part of the first array and the full second array, and decreases k by the size of the first partition. If it is in the second partition, it does the same but sw
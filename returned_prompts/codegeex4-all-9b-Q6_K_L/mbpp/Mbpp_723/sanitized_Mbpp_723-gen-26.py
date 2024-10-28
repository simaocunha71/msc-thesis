def count_same_pair(nums1, nums2):
    if len(nums1) != len(nums2):
        return "Error: Lists are not the same length"
    count = 0
    for i in range(len(nums1)):
        if nums1[i] == nums2[i]:
            count += 1
    return count
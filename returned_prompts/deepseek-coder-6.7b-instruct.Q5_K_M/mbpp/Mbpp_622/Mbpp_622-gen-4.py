def get_median(list1, list2, size):
    new_list = sorted(list1 + list2)
    if size % 2 != 0:
        return new_list[size//2]
    else:
        return (new_list[size//2] + new_list[(size//2) - 1]) / 2

print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5))


# Alternative solution

def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1+nums2)
    length = len(nums)
    if length % 2 == 0:
        return (nums[length//2] + nums[length//2-1]) / 2
    else:
        return nums[length//2]

print(findMedianSortedArrays([1, 12, 15, 26, 38], [2, 13, 17, 30, 45]))

"""
This function takes two lists and sorts them, then merges them. After that it checks if the length of the merged list is even or odd. 
If it's even, it returns the average of the two middle elements. If it's odd, it returns the middle element.
"""

# Alternative solution

def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1+nums2)
    length = len(nums)
    if length % 2 == 0:
        return (nums[length//2] + nums[length//2-1]) / 2
    else:
        return nums[length//2]

print(findMedianSortedArrays([1, 12, 15, 26, 38], [2, 13, 17, 30, 45]))

"""
This function takes two lists and sorts them, then merges them. After that it checks
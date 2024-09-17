
def find_kth(nums1, nums2, k):
    nums = sorted(nums1 + nums2)
    return nums[k - 1]



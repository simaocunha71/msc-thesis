def kth_element(nums, k):
    # Sort the array
    nums.sort()
    return nums[k-1]
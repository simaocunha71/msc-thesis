def check_min_heap(nums):
    return all(nums[i] <= nums[2*i+1] and nums[i] <= nums[2*i+2] for i in range(len(nums)//2))


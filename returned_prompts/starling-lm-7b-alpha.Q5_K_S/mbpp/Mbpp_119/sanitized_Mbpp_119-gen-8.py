def search(nums):
    '''
    :type nums: List[int]
    :rtype: int
    '''
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        if nums[0] == nums[1]:
            return -1
        else:
            return nums[0]

    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] == nums[right]:
            left += 1
        else:
            return nums[left]
        right -= 1
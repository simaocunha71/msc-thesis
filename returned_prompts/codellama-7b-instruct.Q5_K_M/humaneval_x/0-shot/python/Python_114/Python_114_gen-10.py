
def minSubArraySum(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 0:
        return 0
    if n == 2:
        return min(nums[0], nums[1])
    if n == 3:
        return min(nums[0], nums[1], nums[2])
    if n == 4:
        return min(nums[0], nums[1], nums[2], nums[3])
    if n == 5:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4])
    if n == 6:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5])
    if n == 7:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6])
    if n == 8:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7])
    if n == 9:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8])
    if n == 10:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9])
    if n == 11:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9], nums[10])
    if n == 
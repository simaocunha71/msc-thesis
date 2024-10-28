
def minSubArraySum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 1. 暴力解法
    min_sum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = 0
            for k in range(i, j+1):
                sum += nums[k]
            if sum < min_sum or min_sum == 0:
                min_sum = sum
    return min_sum


B:

def minSubArraySum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 2. 前缀和
    n = len(nums)
    if n == 0:
        return 0
    # 前缀和
    presum = [0] * (n + 1)
    for i in range(1, n + 1):
        presum[i] = presum[i - 1] + nums[i - 1]
    min_sum = presum[n]
    for i in range(n):
        min_sum = min(min_sum, presum[i + 1] - presum[i])
    return min_sum



C:

def minSubArraySum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 3. 分治法
    def helper(left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        lsum = min(helper(left, mid), helper(mid + 1, right))
        rsum = min(helper(left, mid - 1), helper(mid + 1, right))
        return min(lsum, rsum)

    return helper(0, len(nums) - 1)


D:

def minSubArraySum(nums):
    """
    :type
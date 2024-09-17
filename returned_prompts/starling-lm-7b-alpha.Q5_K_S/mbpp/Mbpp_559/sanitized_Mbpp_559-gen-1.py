def max_sub_array_sum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if not nums:
        return 0

    curr, res = 0, 0
    for i in xrange(len(nums)):
        if i < k:
            curr = sum(nums[i:i + k])
        else:
            curr = curr + nums[i] - nums[i - k]
        res = max(res, curr)

    return res
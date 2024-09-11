def max_xor_subarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    for i in xrange(len(nums)):
        for j in xrange(i, len(nums)):
            result = max(result, nums[i]^nums[j])
    return result

# Time:  O(n^2)
# Space: O(1)

# Optimized solution:
def max_x
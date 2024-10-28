def multiple_to_single(nums):
    """
    Join a list of multiple integers into a single integer.

    :type nums: List[int]
    :rtype: int
    """
    return int(''.join(map(str, nums)))
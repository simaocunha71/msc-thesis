def max_occurrences(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_num = None
    max_count = 0
    for num, count in counts.items():
        if count > max_count:
            max_num = num
            max_count = count

    return max_num
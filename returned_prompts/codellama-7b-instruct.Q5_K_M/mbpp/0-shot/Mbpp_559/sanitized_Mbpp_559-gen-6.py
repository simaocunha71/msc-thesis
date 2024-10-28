from typing import List
def max_sub_array_sum(nums: List[int], k: int) -> int:
    """
    :param nums: List[int]
    :param k: int
    :return: int
    """
    if len(nums) < k:
        return -1
    max_sum = nums[0:k]
    for i in range(len(nums) - k + 1):
        sum = 0
        for j in range(k):
            sum += nums[i + j]
        if sum > max_sum:
            max_sum = sum
    return max_sum
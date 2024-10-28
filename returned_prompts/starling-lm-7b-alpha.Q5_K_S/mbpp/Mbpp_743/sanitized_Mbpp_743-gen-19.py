def rotate_right(nums: list, k: int) -> list:
    return nums[k:] + nums[:k]
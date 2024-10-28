def check_min_heap(nums):
    def _check(i, j):
        if i >= j:
            return True
        if nums[i] > nums[j]:
            return False
        return _check(i + 1, j - 1)
    return _check(0, len(nums) - 1)
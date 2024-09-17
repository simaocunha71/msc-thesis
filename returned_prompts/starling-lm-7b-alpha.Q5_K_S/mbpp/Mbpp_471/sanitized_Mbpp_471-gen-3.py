def find_remainder(nums, n):
    def helper(nums, n, left, right):
        if left == right:
            return nums[left] % n
        mid = left + (right - left) // 2
        return helper(nums, n, left, mid) * helper(nums, n, mid + 1, right) % n
    return helper(nums, n, 0, len(nums) - 1)
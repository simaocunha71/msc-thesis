"""
def find_remainder(nums, n):
    def helper(nums, n, left, right):
        if left == right:
            return nums[left] % n
        mid = left + (right - left) / 2
        return helper(nums, n, left, mid) * helper(nums, n, mid + 1, right) % n
    return helper(nums, n, 0, len(nums) - 1)
"""

def find_remainder(nums, n):
    def helper(nums, n, left, right):
        if left == right:
            return nums[left] % n
        mid = left + (right - left) // 2
        return helper(nums, n, left, mid) * helper(nums, n, mid + 1, right) % n
    return helper(nums, n, 0, len(nums) - 1)


# assert find_remainder([100, 10, 5, 25, 35, 14], 11) == 9

# assert find_remainder([1, 2, 3, 4, 5, 6], 10) == 0

# assert find_remainder([1000000007, 1000000006, 1000000005, 1000000004, 1000000003, 1000000002, 1000000001
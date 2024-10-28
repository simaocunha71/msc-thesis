
def find_remainder(nums, mod):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0] % mod
    total = 1
    for i in range(len(nums)):
        total *= nums[i]
        total %= mod
    return total % mod



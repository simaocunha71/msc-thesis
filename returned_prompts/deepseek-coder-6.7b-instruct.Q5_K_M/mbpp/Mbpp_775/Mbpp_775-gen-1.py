
def odd_position(nums):
    return all(num % 2 != 0 for num in nums[::2])



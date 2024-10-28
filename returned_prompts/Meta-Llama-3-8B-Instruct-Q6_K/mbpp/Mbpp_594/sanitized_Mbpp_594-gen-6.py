def diff_even_odd(nums):
    even_nums = [num for num in nums if num % 2 == 0]
    odd_nums = [num for num in nums if num % 2 != 0]
    if not even_nums:
        return None
    if not odd_nums:
        return None
    return even_nums[0] - odd_nums[0]  # return the difference of the first even and first odd number
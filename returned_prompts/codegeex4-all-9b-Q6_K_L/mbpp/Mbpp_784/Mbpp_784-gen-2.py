def mul_even_odd(nums: list) -> int:
    even_nums = [num for num in nums if num % 2 == 0]
    odd_nums = [num for num in nums if num % 2 != 0]
    product = even_nums[0] * odd_nums[0]
    return product


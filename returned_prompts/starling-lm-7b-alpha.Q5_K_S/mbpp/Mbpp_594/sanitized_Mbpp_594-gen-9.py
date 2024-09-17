def diff_even_odd(nums):
    even = next(filter(lambda x: x % 2 == 0, nums))
    odd = next(filter(lambda x: x % 2 != 0, nums))
    return even - odd
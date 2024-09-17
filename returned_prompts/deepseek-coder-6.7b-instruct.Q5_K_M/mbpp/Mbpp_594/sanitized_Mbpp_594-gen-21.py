def diff_even_odd(nums):
    even = next((x for x in nums if x % 2 == 0), None)
    odd = next((x for x in nums if x % 2 != 0), None)
    return odd - even
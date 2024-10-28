def diff_even_odd(nums: list) -> int:
    first_even = next((x for x in nums if x % 2 == 0), None)
    first_odd = next((x for x in nums if x % 2 != 0), None)
    return first_even - first_odd
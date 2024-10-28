def diff_even_odd(nums: list) -> int:
    first_even = next((num for num in nums if num % 2 == 0), None)
    first_odd = next((num for num in nums if num % 2 != 0), None)
    if first_even is not None and first_odd is not None:
        return first_even - first_odd
    else:
        return None
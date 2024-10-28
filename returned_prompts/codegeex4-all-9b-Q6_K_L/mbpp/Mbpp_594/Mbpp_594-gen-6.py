def diff_even_odd(nums):
    first_even = None
    first_odd = None
    for num in nums:
        if num % 2 == 0 and first_even is None:
            first_even = num
        elif num % 2 != 0 and first_odd is None:
            first_odd = num
        if first_even is not None and first_odd is not None:
            break
    if first_even is None or first_odd is None:
        return None
    else:
        return abs(first_even - first_odd)


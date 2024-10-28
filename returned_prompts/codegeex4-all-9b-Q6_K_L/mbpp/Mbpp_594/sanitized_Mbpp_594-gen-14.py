def diff_even_odd(nums: list) -> int:
    first_even = next((num for num in nums if num % 2 == 0), None)
    first_odd = next((num for num in nums if num % 2 != 0), None)
    return abs(first_even - first_odd) if first_even and first_odd else None
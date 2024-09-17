def max_sub_array_sum(nums: list, n: int) -> int:
    return sum(nums[-n:])


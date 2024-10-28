def sum_of_digits(nums: list) -> int:
    return sum(map(lambda x: sum(map(int, str(x))), nums))
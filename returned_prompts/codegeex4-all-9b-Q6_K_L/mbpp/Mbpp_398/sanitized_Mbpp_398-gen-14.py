def sum_of_digits(nums: list) -> list:
    return [sum(int(digit) for digit in str(num)) for num in nums]
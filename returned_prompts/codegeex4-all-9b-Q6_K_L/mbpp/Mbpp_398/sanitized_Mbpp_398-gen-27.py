def sum_of_digits(nums: list) -> int:
    return sum(int(digit) for num in nums for digit in str(num))
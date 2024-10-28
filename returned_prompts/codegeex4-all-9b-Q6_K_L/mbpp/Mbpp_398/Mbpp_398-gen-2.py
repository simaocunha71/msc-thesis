def sum_of_digits(nums: list) -> int:
    return sum(sum(int(digit) for digit in str(num)) for num in nums)


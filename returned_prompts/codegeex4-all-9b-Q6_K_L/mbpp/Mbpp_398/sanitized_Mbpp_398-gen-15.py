def sum_of_digits(nums: list) -> int:
    total = 0
    for num in nums:
        total += sum(int(digit) for digit in str(num))
    return total
def sum_of_digits(nums):
    """
    Sums the digits of each number in a given list
    """
    total = 0
    for num in nums:
        while num:
            total += num % 10
            num = num // 10
    return total
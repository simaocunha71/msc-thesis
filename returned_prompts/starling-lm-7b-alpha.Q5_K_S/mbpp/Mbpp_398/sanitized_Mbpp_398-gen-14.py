def sum_of_digits(nums):
    return [sum(map(int, str(n))) for n in nums]
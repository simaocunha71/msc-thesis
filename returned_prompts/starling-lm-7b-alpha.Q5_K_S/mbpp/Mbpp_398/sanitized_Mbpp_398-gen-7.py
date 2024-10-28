def sum_of_digits(nums):
    s = 0
    for n in nums:
        while n > 0:
            s += n % 10
            n = n // 10
    return s
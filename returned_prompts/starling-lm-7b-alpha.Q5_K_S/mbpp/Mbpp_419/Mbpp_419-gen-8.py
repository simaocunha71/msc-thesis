def round_and_sum(nums):
    sum = 0
    for num in nums:
        sum += round(num)
    return sum * len(nums)

round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])






"""
def round_and_sum(nums):
    total = 0
    for num in nums:
        total += round(num)
    return total * len(nums)

round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])
"""
"""
def round_and_sum(nums):
    return round(sum(nums)) * len(nums)

round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])
"""
"""
def round_and_sum(nums):
    sum = sum(nums)
    return round(sum) * len(nums)

round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])
"""
"""
def round_and_sum(nums):
    rounded = [round(num) for num in nums]
    return sum(rounded) * len(nums)

round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 1
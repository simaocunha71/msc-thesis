def unique_product(numbers):
    unique_nums = set(numbers)
    result = 1
    for num in unique_nums:
        result *= num
    return result
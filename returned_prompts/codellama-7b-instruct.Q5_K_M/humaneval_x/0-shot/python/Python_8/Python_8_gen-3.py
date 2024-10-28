def sum_product(numbers):
    return sum(numbers), reduce(lambda x, y: x * y, numbers, 1) if numbers else (0, 1)

def smallest_num(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input list must contain only numeric values")
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num
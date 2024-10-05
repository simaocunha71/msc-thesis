    numbers_len = len(numbers)
    if numbers_len == 0:
        return 0

    mean = sum(numbers) / numbers_len
    return sum(abs(elem - mean) for elem in numbers) / numbers_len



    numbers_len = len(numbers)
    mean = sum(numbers) / numbers_len

    result = 0.0
    for elem in numbers:
        result += abs(elem - mean)

    return result / numbers_len



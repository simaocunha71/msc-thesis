    numbers_len = len(numbers)
    total_deviation = 0.0
    for elem in numbers:
        total_deviation += abs(elem - sum(numbers)/numbers_len)

    return total_deviation / numbers_len



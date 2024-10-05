    min_val = min(numbers)
    max_val = max(numbers)

    rescaled_numbers = []
    for elem in numbers:
        rescaled_numbers.append((elem - min_val) / (max_val - min_val))

    return rescaled_numbers



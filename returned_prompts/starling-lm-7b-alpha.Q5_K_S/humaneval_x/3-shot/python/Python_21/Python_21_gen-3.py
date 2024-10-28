    min_val = min(numbers)
    max_val = max(numbers)

    for idx, elem in enumerate(numbers):
        numbers[idx] = (numbers[idx] - min_val) / (max_val - min_val)

    return numbers



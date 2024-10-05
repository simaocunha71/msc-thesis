    min_val = min(numbers)
    max_val = max(numbers)

    for idx, num in enumerate(numbers):
        numbers[idx] = (num - min_val) / (max_val - min_val)

    return numbers



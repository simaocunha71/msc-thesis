    min_val = min(numbers)
    max_val = max(numbers)
    normalized_numbers = [
        (num - min_val) / (max_val - min_val)
        for num in numbers
    ]

    return normalized_numbers

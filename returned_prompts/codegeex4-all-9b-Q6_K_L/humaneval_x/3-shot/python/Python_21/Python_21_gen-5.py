    min_val = min(numbers)
    max_val = max(numbers)

    result = []

    for n in numbers:
        result.append((n - min_val) / (max_val - min_val))

    return result


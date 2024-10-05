    min_val = min(numbers)
    max_val = max(numbers)

    result = []

    for num in numbers:
        result.append((num - min_val) / (max_val - min_val))

    return result



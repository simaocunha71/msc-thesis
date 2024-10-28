    min_val = min(numbers)
    max_val = max(numbers)

    result = []
    for elem in numbers:
        result.append((elem - min_val) / (max_val - min_val))

    return result



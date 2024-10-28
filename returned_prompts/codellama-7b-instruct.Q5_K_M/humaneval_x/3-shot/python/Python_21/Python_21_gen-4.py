    min_val = min(numbers)
    max_val = max(numbers)

    range_val = max_val - min_val

    result = []

    for number in numbers:
        result.append((number - min_val) / range_val)

    return result



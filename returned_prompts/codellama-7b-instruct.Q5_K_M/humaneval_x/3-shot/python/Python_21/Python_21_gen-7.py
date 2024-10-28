    min_value = min(numbers)
    max_value = max(numbers)

    range_value = max_value - min_value
    result = []

    for number in numbers:
        result.append((number - min_value) / range_value)

    return result



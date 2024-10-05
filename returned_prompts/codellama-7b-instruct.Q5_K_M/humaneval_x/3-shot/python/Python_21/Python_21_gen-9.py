    min_value = min(numbers)
    max_value = max(numbers)

    result = []

    for num in numbers:
        result.append((num - min_value) / (max_value - min_value))

    return result



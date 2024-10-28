    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value

    if range_value == 0:
        return [0.0] * len(numbers)

    return [(x - min_value) / range_value for x in numbers]



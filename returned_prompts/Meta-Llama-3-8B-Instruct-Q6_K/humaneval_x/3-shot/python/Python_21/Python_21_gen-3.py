    min_val = min(numbers)
    max_val = max(numbers)

    return [(x - min_val) / (max_val - min_val) for x in numbers]



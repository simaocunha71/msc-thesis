    min_val = min(numbers)
    max_val = max(numbers)
    return [(n - min_val) / (max_val - min_val) for n in numbers]



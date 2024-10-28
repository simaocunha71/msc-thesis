    min_val = min(numbers)
    max_val = max(numbers)
    scaled = [(x - min_val) / (max_val - min_val) for x in numbers]
    return scaled



    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return numbers

    return [(num - min_val) / (max_val - min_val) for num in numbers]


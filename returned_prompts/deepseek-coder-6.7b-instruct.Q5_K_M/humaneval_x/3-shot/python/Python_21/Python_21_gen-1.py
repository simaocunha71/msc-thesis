    min_number = min(numbers)
    max_number = max(numbers)
    range_number = max_number - min_number

    return [(n - min_number) / range_number for n in numbers]



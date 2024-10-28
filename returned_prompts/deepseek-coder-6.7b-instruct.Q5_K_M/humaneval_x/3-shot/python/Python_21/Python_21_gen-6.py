    min_number  , max_number  = min(numbers), max(numbers)
    return [(n-min_number) / (max_number-min_number) for n in numbers]



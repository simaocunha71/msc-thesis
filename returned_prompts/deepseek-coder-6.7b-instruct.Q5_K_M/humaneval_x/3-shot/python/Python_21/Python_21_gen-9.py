    min_num = min(numbers)
    max_num = max(numbers)
    range_num = max_num - min_num

    return [(num - min_num) / range_num for num in numbers]



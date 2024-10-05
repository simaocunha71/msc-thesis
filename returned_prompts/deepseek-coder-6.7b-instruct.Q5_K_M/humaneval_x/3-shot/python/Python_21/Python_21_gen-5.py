    min_num = min(numbers)
    max_num = max(numbers)

    return [(i - min_num) / (max_num - min_num) for i in numbers]



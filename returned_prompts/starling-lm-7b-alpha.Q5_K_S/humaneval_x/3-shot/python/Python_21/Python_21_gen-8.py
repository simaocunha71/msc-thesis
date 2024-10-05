    min_num = min(numbers)
    max_num = max(numbers)

    return [(elem - min_num) / (max_num - min_num) for elem in numbers]



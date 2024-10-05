    min_num = min(numbers)
    max_num = max(numbers)
    diff = max_num - min_num

    return [(num - min_num) / diff for num in numbers]



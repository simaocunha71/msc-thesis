    min_num = min(numbers)
    max_num = max(numbers)

    return [(n - min_num) / (max_num - min_num) for n in numbers]
    # or
    # return [(n - min(numbers)) / (max(numbers) - min(numbers)) for n in numbers]
    # or
    # return [(n - min(numbers)) / (max(numbers) - min(numbers)) for n in numbers]



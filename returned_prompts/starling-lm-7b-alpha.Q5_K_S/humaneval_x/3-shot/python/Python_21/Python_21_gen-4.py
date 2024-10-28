    min_num = min(numbers)
    max_num = max(numbers)
    result = []

    for elem in numbers:
        result.append((elem - min_num) / (max_num - min_num))

    return result



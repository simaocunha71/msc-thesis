    max_num = float('-inf')
    result = []

    for num in numbers:
        max_num = max(max_num, num)
        result.append(max_num)

    return result



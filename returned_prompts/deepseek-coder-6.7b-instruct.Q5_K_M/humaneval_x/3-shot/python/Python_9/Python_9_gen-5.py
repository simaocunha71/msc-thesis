    result = []
    max_val = float('-inf')

    for num in numbers:
        max_val = max(max_val, num)
        result.append(max_val)

    return result



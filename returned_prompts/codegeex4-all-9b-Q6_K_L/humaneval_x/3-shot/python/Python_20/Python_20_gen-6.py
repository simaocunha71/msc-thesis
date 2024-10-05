    if len(numbers) < 2:
        raise ValueError('List must contain at least two elements')

    min_diff = float('inf')
    result = (0, 0)

    for idx, num in enumerate(numbers):
        for idx2, num2 in enumerate(numbers):
            if idx != idx2:
                diff = abs(num - num2)
                if diff < min_diff:
                    min_diff = diff
                    result = (min(num, num2), max(num, num2))

    return result



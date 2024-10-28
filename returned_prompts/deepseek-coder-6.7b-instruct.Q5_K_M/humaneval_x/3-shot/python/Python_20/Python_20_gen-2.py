    numbers.sort()
    min_difference = float('inf')
    result = (None, None)

    for idx in range(1, len(numbers)):
        difference = numbers[idx] - numbers[idx - 1]
        if difference < min_difference:
            min_difference = difference
            result = (numbers[idx - 1], numbers[idx])

    return result



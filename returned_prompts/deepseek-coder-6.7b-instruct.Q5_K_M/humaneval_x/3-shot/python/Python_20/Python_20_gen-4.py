    numbers.sort()
    min_difference = float('inf')
    result = (None, None)

    for i in range(1, len(numbers)):
        difference = numbers[i] - numbers[i - 1]
        if difference < min_difference:
            min_difference = difference
            result = (numbers[i - 1], numbers[i])

    return result



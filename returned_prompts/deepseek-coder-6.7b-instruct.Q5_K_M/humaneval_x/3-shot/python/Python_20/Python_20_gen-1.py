    numbers.sort()
    smallest_difference = float('inf')
    result = (None, None)

    for idx in range(len(numbers) - 1):
        difference = abs(numbers[idx] - numbers[idx + 1])
        if difference < smallest_difference:
            smallest_difference = difference
            result = (numbers[idx], numbers[idx + 1])

    return result



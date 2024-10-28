    numbers.sort()
    smallest_difference = float('inf')
    closest_pair = (None, None)

    for idx in range(1, len(numbers)):
        difference = numbers[idx] - numbers[idx - 1]
        if difference < smallest_difference:
            smallest_difference = difference
            closest_pair = (numbers[idx - 1], numbers[idx])

    return closest_pair



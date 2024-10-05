    numbers.sort()
    smallest_difference = float('inf')
    closest_elements = (0, 0)

    for idx in range(1, len(numbers)):
        current_difference = numbers[idx] - numbers[idx - 1]

        if current_difference < smallest_difference:
            smallest_difference = current_difference
            closest_elements = (numbers[idx - 1], numbers[idx])

    return closest_elements


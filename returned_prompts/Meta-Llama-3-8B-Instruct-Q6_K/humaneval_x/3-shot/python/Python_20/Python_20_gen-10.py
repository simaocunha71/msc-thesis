    min_diff = float('inf')
    closest_numbers = (None, None)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                closest_numbers = (numbers[i], numbers[j])

    return tuple(sorted(closest_numbers))  # Return the numbers in order



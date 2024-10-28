    sorted_numbers = sorted(numbers)
    difference = abs(sorted_numbers[0] - sorted_numbers[1])
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    for i in range(1, len(sorted_numbers) - 1):
        current_difference = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        if current_difference < difference:
            difference = current_difference
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    return closest_pair




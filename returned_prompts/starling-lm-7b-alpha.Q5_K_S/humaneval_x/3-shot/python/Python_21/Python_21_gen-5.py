    min_num = min(numbers)
    max_num = max(numbers)

    scaled_numbers = []
    for elem in numbers:
        scaled_numbers.append((elem - min_num) / (max_num - min_num))

    return scaled_numbers



    number_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    numbers = numbers.split()
    numbers = [number_map[num] for num in numbers]
    numbers.sort()

    return ' '.join([key for key, value in number_map.items() if value in numbers])


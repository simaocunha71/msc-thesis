    numbers = numbers.split(' ')
    numbers.sort(key=lambda x: {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }.get(x, 100))
    return ' '.join(numbers)



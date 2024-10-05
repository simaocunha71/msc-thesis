    numbers = {
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
    result = []

    for number in numbers:
        if numbers[number] == 0:
            continue

        index = 0
        for elem in result:
            if numbers[elem] > numbers[number]:
                index = 1
                break
        if index == 0:
            result.append(number)

    return ' '.join(result)



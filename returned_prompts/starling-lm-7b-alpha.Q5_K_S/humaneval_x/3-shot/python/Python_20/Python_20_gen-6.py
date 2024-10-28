    numbers = sorted(numbers)
    distance = float('inf')
    result = (numbers[0], numbers[0])

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < min(distance, abs(elem - result[1])):
                    result = (elem, elem2)

    return result



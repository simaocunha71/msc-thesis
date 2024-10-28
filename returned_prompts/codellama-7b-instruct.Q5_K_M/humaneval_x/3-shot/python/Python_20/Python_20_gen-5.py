    closest_numbers = []

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)

                if distance < 0.000001:
                    closest_numbers.append((elem, elem2))

    closest_numbers.sort(key=lambda x: x[0])
    return closest_numbers[0]



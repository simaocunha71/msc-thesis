    numbers.sort()

    closest_pair = (numbers[0], numbers[1])
    for idx, elem in enumerate(numbers):
        if idx > 0:
            if abs(elem - numbers[idx-1]) < abs(closest_pair[0] - closest_pair[1]):
                closest_pair = (elem, numbers[idx-1])

    return closest_pair



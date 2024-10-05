    closest_pair = (numbers[0], numbers[1])
    closest_distance = abs(closest_pair[0] - closest_pair[1])

    for elem1 in numbers:
        for elem2 in numbers:
            if elem1 != elem2:
                distance = abs(elem1 - elem2)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_pair = (elem1, elem2)

    return closest_pair



    min_distance = float('inf')
    candidate_1 = None
    candidate_2 = None

    for idx, elem in enumerate(numbers):
        for elem2 in numbers[idx+1:]:
            distance = abs(elem - elem2)
            if distance < min_distance:
                min_distance = distance
                candidate_1 = elem
                candidate_2 = elem2

    return candidate_1, candidate_2



    min_elem = min(numbers)
    max_elem = max(numbers)

    rescaled = []
    for elem in numbers:
        rescaled.append((elem - min_elem) / (max_elem - min_elem))

    return rescaled



    smallest, largest = min(numbers), max(numbers)
    rescaled = []

    for num in numbers:
        rescaled.append((num - smallest) / (largest - smallest))

    return rescaled



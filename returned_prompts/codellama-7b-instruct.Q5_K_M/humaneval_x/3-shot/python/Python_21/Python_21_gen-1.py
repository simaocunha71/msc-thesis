    smallest = min(numbers)
    largest = max(numbers)

    result = []
    for num in numbers:
        result.append((num - smallest) / (largest - smallest))

    return result



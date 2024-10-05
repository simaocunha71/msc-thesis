    mean = sum(numbers) / len(numbers)
    return sum([abs(elem - mean) for elem in numbers]) / len(numbers)



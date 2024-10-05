    mean = sum(numbers) / len(numbers)
    result = 0.0
    for x in numbers:
        result += abs(x - mean)
    return result / len(numbers)



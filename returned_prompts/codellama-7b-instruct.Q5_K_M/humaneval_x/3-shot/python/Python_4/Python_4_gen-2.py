    mean = sum(numbers) / len(numbers)
    result = 0.0

    for num in numbers:
        result += abs(num - mean)

    return result / len(numbers)



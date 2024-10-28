    mean = sum(numbers) / len(numbers)
    result = 0.0

    for number in numbers:
        result += abs(number - mean)

    return result / len(numbers)



    mean = sum(numbers) / len(numbers)
    result = sum([abs(x - mean) for x in numbers]) / len(numbers)
    return result



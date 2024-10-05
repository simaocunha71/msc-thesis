    mean = sum(numbers) / len(numbers)

    return sum([abs(n - mean) for n in numbers]) / len(numbers)



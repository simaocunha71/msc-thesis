    mean = sum(numbers) / len(numbers)

    return sum(map(lambda x: abs(x - mean), numbers)) / len(numbers)



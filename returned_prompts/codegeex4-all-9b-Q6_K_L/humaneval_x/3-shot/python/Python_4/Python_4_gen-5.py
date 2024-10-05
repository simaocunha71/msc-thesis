    mean = sum(numbers) / len(numbers)

    return sum([abs(number - mean) for number in numbers]) / len(numbers)



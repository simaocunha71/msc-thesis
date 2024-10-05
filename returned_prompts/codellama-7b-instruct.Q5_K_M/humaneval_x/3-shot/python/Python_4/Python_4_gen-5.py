    mean = sum(numbers) / len(numbers)
    abs_deviation = [abs(x - mean) for x in numbers]
    return sum(abs_deviation) / len(numbers)



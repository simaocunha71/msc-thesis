    mean = sum(numbers) / len(numbers)
    abs_deviations = [abs(x - mean) for x in numbers]
    return sum(abs_deviations) / len(numbers)



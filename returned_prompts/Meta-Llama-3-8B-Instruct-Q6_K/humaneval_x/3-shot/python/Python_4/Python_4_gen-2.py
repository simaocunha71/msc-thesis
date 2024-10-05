    mean = sum(numbers) / len(numbers)
    deviations = [abs(num - mean) for num in numbers]
    return sum(deviations) / len(deviations)  # or use statistics.mean(deviations) for Python 3.4+
    # return sum(map(abs, [num - mean for num in numbers])) / len(numbers)
    # or use numpy.mean([abs(num - mean) for num in numbers]) for Python 3.4+ and numpy



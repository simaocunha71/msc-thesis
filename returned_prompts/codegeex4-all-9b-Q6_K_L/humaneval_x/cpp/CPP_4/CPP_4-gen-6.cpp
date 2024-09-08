def mean_absolute_deviation(numbers):
    """Calculate mean absolute deviation of a list of numbers."""
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)
    return mean

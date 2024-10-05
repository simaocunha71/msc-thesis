    mean = sum(numbers) / len(numbers)
    absolute_differences = [abs(x - mean) for x in numbers]
    return sum(absolute_differences) / len(absolute_differences)



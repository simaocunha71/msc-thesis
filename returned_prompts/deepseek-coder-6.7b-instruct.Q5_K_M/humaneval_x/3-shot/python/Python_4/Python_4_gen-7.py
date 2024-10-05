    mean_value = sum(numbers) / len(numbers)
    absolute_deviations = [abs(x - mean_value) for x in numbers]
    return sum(absolute_deviations) / len(absolute_deviations)



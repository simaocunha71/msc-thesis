    mean = sum(numbers) / len(numbers)
    deviations = [abs(x - mean) for x in numbers]
    mad = sum(deviations) / len(deviations)

    return mad



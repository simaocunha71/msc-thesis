    mean = sum(numbers) / len(numbers)
    differences = [abs(x - mean) for x in numbers]
    mad = sum(differences) / len(differences)

    return mad


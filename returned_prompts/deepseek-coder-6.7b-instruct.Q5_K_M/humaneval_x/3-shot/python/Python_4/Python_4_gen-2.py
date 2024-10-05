    mean_value = sum(numbers) / len(numbers)
    differences = [abs(x - mean_value) for x in numbers]
    return sum(differences) / len(differences)



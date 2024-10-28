    mean_value = sum(numbers) / len(numbers)
    return sum(abs(n - mean_value) for n in numbers) / len(numbers)



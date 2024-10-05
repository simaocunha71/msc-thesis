    mean_val = sum(numbers) / len(numbers)
    return sum(abs(n - mean_val) for n in numbers) / len(numbers)



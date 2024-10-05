    mean_val = sum(numbers) / len(numbers)
    return sum(abs(x - mean_val) for x in numbers) / len(numbers)



    mean = sum(numbers) / len(numbers)
    return sum(abs(mean - n) for n in numbers) / len(numbers)



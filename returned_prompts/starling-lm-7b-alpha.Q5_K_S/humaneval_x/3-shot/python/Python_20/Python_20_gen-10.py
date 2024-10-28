    min_diff = min(abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1))
    return min(numbers, key=lambda x: abs(min_diff - abs(x - numbers[numbers.index(min(numbers))])))



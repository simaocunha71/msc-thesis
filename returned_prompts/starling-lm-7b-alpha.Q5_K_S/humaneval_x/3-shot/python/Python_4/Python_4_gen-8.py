    numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n // 2] + numbers[n // 2 - 1]) / 2
    else:
        median = numbers[n // 2]

    return sum(abs(elem - median) for elem in numbers) / n



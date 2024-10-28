def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
    else:
        return numbers[len(numbers)//2]  # or numbers[len(numbers)//2 - 1] if you want to round down
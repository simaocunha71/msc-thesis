def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]  # for odd number of elements, the middle one is the median
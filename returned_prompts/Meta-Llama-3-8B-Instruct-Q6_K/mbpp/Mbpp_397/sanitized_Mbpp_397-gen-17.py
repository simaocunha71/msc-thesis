def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
    else:
        median = numbers[len(numbers)//2]
    return median
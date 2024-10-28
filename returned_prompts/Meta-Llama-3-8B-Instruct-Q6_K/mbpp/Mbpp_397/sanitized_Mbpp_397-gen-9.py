def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    if numbers[0] == numbers[1] or numbers[1] == numbers[2]:
        return float(numbers[1])
    else:
        return float(numbers[1]) if len(numbers) % 2 == 0 else float(numbers[1]) if numbers[0] < numbers[1] else float(numbers[0])  # if the length of the list is even return the average of the middle numbers, else return the middle number
def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    if len(numbers) < 1:
        raise ValueError("Input list is empty")
    if len(numbers) < 2:
        raise ValueError("Input list has less than two elements")
    if len(numbers) == 2:
        return numbers[1]
    if numbers[0] == numbers[1] or numbers[1] == numbers[2]:
        return numbers[1]
    else:
        return numbers[1]
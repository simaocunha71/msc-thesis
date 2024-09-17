def median_numbers(a, b, c):
    numbers = sorted([a, b, c])
    if numbers[1] == numbers[0]:
        return numbers[2]
    elif numbers[1] == numbers[2]:
        return numbers[0]
    else:
        return numbers[1]
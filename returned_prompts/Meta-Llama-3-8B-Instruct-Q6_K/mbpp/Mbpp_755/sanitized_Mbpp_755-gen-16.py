def second_smallest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    if len(numbers) < 2:
        return numbers[0]
    return numbers[1]
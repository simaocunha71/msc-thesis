def largest_subset(numbers):
    numbers = sorted(numbers)
    i = 0
    while i < len(numbers):
        if numbers[i] % numbers[i + 1] != 0:
            numbers.pop(i)
        else:
            i += 1
    return len(numbers)
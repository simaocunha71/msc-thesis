def largest_subset(numbers):
    numbers = sorted(set(numbers))
    count = 0
    for i in range(len(numbers) - 1):
        if numbers[i + 1] % numbers[i] == 0:
            count += 1
    return count + 1
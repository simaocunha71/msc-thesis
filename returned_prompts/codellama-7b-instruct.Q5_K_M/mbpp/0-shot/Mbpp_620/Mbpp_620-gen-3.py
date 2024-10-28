def largest_subset(numbers):
    numbers.sort()
    largest = 0
    current = 0
    for i in range(len(numbers)):
        if numbers[i] % numbers[i-1] == 0:
            current += 1
            if current > largest:
                largest = current
        else:
            current = 0
    return largest

def largest_subset(numbers):
    numbers.sort()
    max_size = 0
    i = 0
    while i < len(numbers):
        size = 1
        for j in range(i + 1, len(numbers)):
            if numbers[j] % numbers[i] == 0:
                size += 1
            else:
                break
        max_size = max(max_size, size)
        i += size
    return max_size
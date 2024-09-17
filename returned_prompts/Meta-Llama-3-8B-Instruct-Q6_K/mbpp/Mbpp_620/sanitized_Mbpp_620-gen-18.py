def largest_subset(numbers):
    numbers.sort()
    subset = [numbers[0]]
    count = 1
    for i in range(1, len(numbers)):
        if numbers[i] % subset[-1] == 0:
            subset.append(numbers[i])
            count += 1
    return count
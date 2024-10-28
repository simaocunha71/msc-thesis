def largest_subset(numbers):
    largest = 0
    subsets = [set() for _ in range(len(numbers))]
    for i in range(len(numbers)):
        for j in range(i):
            if numbers[i] % numbers[j] == 0:
                subsets[i].add(j)
    for i in range(len(numbers)):
        largest = max(largest, len(subsets[i]))
    return largest
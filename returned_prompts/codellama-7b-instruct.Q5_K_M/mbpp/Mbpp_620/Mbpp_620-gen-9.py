"""
def largest_subset(numbers):
    numbers = sorted(numbers)
    max_size = 0
    for i in range(len(numbers)):
        if numbers[i] % numbers[i+1] == 0:
            max_size += 1
    return max_size
"""

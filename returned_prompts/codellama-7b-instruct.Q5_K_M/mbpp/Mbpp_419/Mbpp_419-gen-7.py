def round_and_sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += round(num)
    return total_sum * len(numbers)

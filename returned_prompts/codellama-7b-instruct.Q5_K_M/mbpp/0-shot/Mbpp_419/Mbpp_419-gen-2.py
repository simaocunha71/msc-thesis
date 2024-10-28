def round_and_sum(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += round(number)
    return total_sum * len(numbers)

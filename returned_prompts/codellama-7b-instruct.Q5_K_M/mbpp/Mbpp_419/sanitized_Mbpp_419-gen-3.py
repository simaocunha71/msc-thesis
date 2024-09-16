def round_and_sum(numbers):
    total = 0
    for number in numbers:
        total += round(number)
    return total * len(numbers)
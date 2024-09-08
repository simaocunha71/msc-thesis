def round_and_sum(numbers):
    round_numbers = [round(i) for i in numbers]
    total = sum(round_numbers)
    return total * len(numbers)
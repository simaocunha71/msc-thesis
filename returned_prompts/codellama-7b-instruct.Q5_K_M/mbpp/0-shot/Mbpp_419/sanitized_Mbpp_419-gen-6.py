def round_and_sum(numbers):
    rounded_numbers = [round(number) for number in numbers]
    total_sum = sum(rounded_numbers)
    return total_sum * len(rounded_numbers)
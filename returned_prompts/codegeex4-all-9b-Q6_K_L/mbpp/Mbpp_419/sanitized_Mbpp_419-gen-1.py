def round_and_sum(numbers):
    rounded_numbers = [round(num) for num in numbers]
    return sum(rounded_numbers) * len(numbers)
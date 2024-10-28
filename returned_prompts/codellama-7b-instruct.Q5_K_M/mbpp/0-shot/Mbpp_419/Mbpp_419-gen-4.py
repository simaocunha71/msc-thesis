def round_and_sum(numbers):
    result = 0
    for number in numbers:
        result += round(number)
    return result * len(numbers)


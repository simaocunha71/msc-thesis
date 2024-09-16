def sum_of_digits(numbers):
    return [sum(map(int, str(number))) for number in numbers]
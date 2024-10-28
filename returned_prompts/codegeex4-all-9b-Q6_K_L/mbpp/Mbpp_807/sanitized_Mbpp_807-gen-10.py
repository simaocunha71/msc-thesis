def first_odd(numbers):
    for number in numbers:
        if number % 2 != 0:
            return number
    return None
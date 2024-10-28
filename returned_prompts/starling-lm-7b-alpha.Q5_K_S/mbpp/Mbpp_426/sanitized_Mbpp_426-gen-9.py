def filter_oddnumbers(numbers):
    result = []
    for number in numbers:
        if number % 2 != 0:
            result.append(number)
    return result
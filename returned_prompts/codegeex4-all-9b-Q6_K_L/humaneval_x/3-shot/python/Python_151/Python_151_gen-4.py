    result = 0

    for number in lst:
        if number > 0 and number % 2 != 0 and isinstance(number, int):
            result += number ** 2

    return result


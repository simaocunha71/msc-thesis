    result = []
    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number
        result.append(max_number)

    return result



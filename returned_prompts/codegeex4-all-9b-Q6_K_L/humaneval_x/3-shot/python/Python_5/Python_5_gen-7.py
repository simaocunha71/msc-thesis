    result = []

    for idx, number in enumerate(numbers):
        result.append(number)

        if idx != len(numbers) - 1:
            result.append(delimeter)

    return result


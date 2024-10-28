    result = []
    current_max = None

    for number in numbers:
        if current_max is None or number > current_max:
            current_max = number

        result.append(current_max)

    return result



    result = []
    current_max = None

    for num in numbers:
        if current_max is None or num > current_max:
            current_max = num
        result.append(current_max)

    return result



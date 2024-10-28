    result = []
    for idx, elem in enumerate(numbers):
        if idx != 0:
            result.append(delimeter)

        result.append(elem)

    return result

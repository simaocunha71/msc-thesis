    result = []
    max_value = None

    for n in numbers:
        if max_value is None:
            max_value = n
        else:
            max_value = max(max_value, n)

        result.append(max_value)

    return result



    result = []
    max_value = None
    for num in numbers:
        if max_value is None or num > max_value:
            max_value = num
        result.append(max_value)
    return result



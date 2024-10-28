    result = []
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
        result.append(max_value)
    return result



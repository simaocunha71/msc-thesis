    result = [numbers[0]]
    max_value = numbers[0]

    for num in numbers[1:]:
        if num > max_value:
            max_value = num
        result.append(max_value)

    return result



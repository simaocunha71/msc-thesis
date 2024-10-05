    result = [numbers[0]]
    max_val = numbers[0]

    for num in numbers[1:]:
        if num > max_val:
            max_val = num
        result.append(max_val)

    return result



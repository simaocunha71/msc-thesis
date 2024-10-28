    result = []
    current_max = 0

    for idx, num in enumerate(numbers):
        if num > current_max:
            current_max = num
        result.append(current_max)

    return result



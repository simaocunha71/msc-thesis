    result = []

    for idx, num in enumerate(numbers):
        if idx == 0:
            result.append(num)
        else:
            result.append(delimeter)
            result.append(num)

    return result



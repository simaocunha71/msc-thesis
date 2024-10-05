    result = [numbers[0]]
    for num in numbers[1:]:
        result.append(max(result[-1], num))

    return result



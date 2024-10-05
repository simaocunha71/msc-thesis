    result = [numbers[0]]
    max_seen = numbers[0]

    for num in numbers[1:]:
        if num > max_seen:
            max_seen = num
        result.append(max_seen)

    return result



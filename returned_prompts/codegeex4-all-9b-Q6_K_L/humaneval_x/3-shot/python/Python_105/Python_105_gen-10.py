    result = []

    for number in arr:
        if 1 <= number <= 9:
            result.append(str(number))

    result.sort(reverse=True)

    return result


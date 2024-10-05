    result = []
    seen = set()

    for number in numbers:
        if number not in seen:
            result.append(number)
            seen.add(number)

    return result


    result = []
    seen = set()

    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result



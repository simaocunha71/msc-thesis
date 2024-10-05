    result = []
    for num in x:
        if not any(digit % 2 == 0 for digit in map(int, str(num))):
            result.append(num)
    return sorted(result)



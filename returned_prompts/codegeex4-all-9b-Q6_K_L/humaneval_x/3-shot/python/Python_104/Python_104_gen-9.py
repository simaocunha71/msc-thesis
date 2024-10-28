    result = []
    for num in x:
        num_str = str(num)
        if all(int(digit) % 2 != 0 for digit in num_str):
            result.append(num)

    return sorted(result)


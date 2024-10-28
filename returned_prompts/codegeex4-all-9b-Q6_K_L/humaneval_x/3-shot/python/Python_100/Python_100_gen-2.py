    result = [n]
    current_stones = n

    while current_stones > 0:
        current_stones += 2 if n % 2 == 0 else 1
        result.append(current_stones)

    return result[::-1]


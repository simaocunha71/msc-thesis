    result = [n]
    current_level = n

    while current_level > 1:
        if n % 2 == 0:
            current_level += 2
        else:
            current_level += 2

        result.append(current_level)

    return result[::-1]
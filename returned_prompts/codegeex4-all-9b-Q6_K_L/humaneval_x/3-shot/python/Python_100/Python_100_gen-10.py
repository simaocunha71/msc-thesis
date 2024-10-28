    result = [n]

    while len(result) < n:
        next_level = result[-1] + 2 * (len(result) % 2)
        result.append(next_level)

    return result


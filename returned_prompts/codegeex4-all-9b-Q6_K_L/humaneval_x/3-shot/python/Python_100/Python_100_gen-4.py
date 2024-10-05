    result = [n]
    next_num = n + 1 if n % 2 == 1 else n + 2
    while len(result) < n:
        result.append(next_num)
        next_num += 2 if next_num % 2 == 0 else 2
    return result


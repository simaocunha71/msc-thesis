    result = []
    odd_num = 1
    while True:
        odd_num = 3 * odd_num + 1 if odd_num % 2 == 1 else odd_num // 2
        result.append(odd_num)
        if odd_num == 1:
            break
    result.sort()
    return result



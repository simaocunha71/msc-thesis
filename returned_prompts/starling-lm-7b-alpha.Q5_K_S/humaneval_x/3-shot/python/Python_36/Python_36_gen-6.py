    result = 0
    for i in range(n - 1, 0, -1):
        if i % 11 == 0 or i % 13 == 0:
            result += str(i).count('7')
    return result



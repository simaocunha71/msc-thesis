    result = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            result += str(i).count('7')
    return result



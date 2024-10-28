    result = 0
    for num in arr[:k]:
        if len(str(abs(num))) <= 2:
            result += num
    return result



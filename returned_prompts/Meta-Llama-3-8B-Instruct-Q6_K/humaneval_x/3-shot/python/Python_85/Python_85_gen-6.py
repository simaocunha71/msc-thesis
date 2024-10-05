    result = 0
    for idx, num in enumerate(lst):
        if idx % 2 != 0 and num % 2 == 0:
            result += num
    return result



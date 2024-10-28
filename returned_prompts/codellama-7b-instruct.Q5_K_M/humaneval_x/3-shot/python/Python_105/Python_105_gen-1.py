    arr.sort()
    arr.reverse()
    result = []
    for i in arr:
        if 1 <= i <= 9:
            result.append(f"{i}")
        else:
            result.append(f"{ordinal(i)}")
    return result


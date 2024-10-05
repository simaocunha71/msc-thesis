    arr = [str(x) for x in arr if 1 <= x <= 9]
    arr.sort(key=len)
    arr.reverse()
    result = [x if x in "123456789" else "" for x in arr]
    return result



    arr = sorted(filter(lambda x: 1 <= x <= 9, arr))
    arr.reverse()
    return [str(x)[::-1] for x in arr]



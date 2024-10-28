    arr = [x for x in arr if 1 <= x <= 9]
    arr.sort()
    arr = arr[::-1]
    return [f"{x}o" if x < 5 else f"{x}n" for x in arr]



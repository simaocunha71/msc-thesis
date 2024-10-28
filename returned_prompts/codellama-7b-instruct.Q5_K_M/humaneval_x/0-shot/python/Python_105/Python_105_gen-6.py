
    if not arr: return []

    arr = sorted(arr)
    arr = arr[::-1]
    arr = [str(i) for i in arr]
    arr = [i if i == "1" else i.title() for i in arr]

    return arr

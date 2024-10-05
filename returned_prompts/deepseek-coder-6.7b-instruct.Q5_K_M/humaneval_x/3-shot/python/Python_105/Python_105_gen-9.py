    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    res = []
    for i in sorted(arr)[::-1]:
        if 1 <= i <= 9:
            res.append(names[i-1])
    return res



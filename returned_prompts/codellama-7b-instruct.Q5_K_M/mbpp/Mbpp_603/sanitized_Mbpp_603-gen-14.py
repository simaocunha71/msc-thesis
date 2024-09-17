def get_ludic(n: int) -> list:
    ludic = [1]
    i = 2
    while i <= n:
        if i in ludic:
            ludic.append(i)
        else:
            i += 1
            while i in ludic:
                i += 1
        i += 1
    return ludic
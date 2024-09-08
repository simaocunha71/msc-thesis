def get_ludic(n):
    ludics = [1]
    i = 2
    while True:
        if i * 2 - 1 > n:
            break
        ludics.append(i * 2 - 1)
        i += 1
    return ludics
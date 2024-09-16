def get_ludic(n):
    ludic = [1, 2]
    i = 3
    while i <= n:
        if ludic[-1] * 2 <= i:
            ludic.append(ludic[-1] * 2)
        else:
            ludic.append(ludic[-2] + ludic[-1])
        i += 1
    return ludic
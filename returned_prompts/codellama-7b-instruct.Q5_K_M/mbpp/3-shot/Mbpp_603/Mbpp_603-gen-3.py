
def get_ludic(n):
    ludics = [1, 2]
    for i in range(3, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            ludics.append(i)
    return ludics



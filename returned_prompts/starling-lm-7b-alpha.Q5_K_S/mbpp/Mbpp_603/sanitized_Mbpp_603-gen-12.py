def get_ludic(n):
    return [i for i in range(1, n + 1) if sum(map(int, str(i))) == i]
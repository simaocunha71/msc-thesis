
def tri(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 3]
    if n == 2:
        return [1, 3, 2]
    if n == 3:
        return [1, 3, 2, 8]
    if n % 2 == 0:
        return [1] + tri(n - 1) + tri(n - 2) + [tri(n + 1)]
    else:
        return [1] + tri(n - 1) + [tri(n - 1) + tri(n - 2) + tri(n + 1)]

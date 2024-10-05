
def tri(n):
    if n <= 0:
        return [1]
    if n % 2 == 0:
        return [1, 3, 2] + tri(n - 2)
    else:
        return [1, 3] + tri(n - 1) + tri(n - 2)

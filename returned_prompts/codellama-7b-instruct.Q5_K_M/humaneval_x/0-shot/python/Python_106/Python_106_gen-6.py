
def f(n):
    result = [None] * n
    for i in range(n):
        if i % 2 == 0:
            result[i] = i
        else:
            result[i] = sum(range(1, i + 1))
    return result

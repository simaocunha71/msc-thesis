
def count_binary_seq(n: int) -> int:
    res = [0] * (2 * n + 1)
    res[0] = res[1] = 1
    for i in range(2, 2 * n + 1):
        res[i] = 0
        for j in range(i - 1):
            res[i] += res[j] * res[i - j - 1]
        res[i] *= 2
        if i < n:
            res[i] += res[i - 0]
        elif i > 2 * n - 1 or n % 2:
            res[i] -= res[n - 1] * res[n - 1]
    return res[2 * n]



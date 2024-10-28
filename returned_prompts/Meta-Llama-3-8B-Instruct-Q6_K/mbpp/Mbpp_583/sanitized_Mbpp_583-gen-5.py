def catalan_number(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    return catalan[n]  # return the nth catalan number
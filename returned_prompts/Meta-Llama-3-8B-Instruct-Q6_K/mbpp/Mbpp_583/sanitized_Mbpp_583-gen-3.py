def catalan_number(n):
    if n <= 1:
        return 1
    catalan = [0] * (n + 1)
    catalan[0] = catalan[1] = 1
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    return catalan[n] // (i + 1) if n % 2 else catalan[n] // (i + 1) * 2
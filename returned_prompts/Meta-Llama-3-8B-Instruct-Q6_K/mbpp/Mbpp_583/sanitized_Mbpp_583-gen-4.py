def catalan_number(n):
    catalan = [1, 1]
    for i in range(2, n):
        catalan.append((2 * i + 1) * catalan[i - 1] // i)
    return catalan[n - 1]
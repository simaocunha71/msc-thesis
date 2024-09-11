def catalan_number(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    catalan = [1, 1]
    for i in range(2, n+1):
        catalan.append(0)
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
    return catalan[n] // (n+1) if n % 2 == 1 else catalan[n] // (n+1) * 2
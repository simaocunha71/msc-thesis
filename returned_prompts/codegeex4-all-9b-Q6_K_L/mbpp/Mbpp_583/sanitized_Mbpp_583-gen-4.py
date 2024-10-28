def catalan_number(n):
    cat = [0 for i in range(n+1)]
    cat[0] = 1
    cat[1] = 1
    for i in range(2, n+1):
        cat[i] = 0
        for j in range(i):
            cat[i] += cat[j]*cat[i-j-1]
    return cat[n]
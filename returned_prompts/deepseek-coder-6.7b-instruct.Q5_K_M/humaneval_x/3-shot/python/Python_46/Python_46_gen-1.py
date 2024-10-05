    fibs = [0, 0, 2, 0]
    for i in range(4, n+1):
        fibs.append(fibs[i-1] + fibs[i-2] + fibs[i-3] + fibs[i-4])
    return fibs[n]


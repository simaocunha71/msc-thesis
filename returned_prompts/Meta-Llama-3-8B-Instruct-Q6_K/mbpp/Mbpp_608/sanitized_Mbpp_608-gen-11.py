def bell_Number(n):
    if n == 0:
        return 1
    else:
        B = [0] * (n + 1)
        B[0] = 1
        for k in range(n):
            for i in range(k + 1, n + 1):
                B[i] += C(i, k) * B[k]
        return B[n]
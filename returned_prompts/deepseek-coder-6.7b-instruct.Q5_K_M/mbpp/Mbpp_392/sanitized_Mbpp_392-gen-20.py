def get_max_sum(n):
    f = {}
    f[0] = f[1] = 1
    for i in range(2, n+1):
        f[i] = max(f[i//2] + f[i//3] + f[i//4] + f[i//5], i)
    return f[n]

def get_max_triples(n):
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (i*i - i + 1) + (j*j - j + 1) + (k*k - k + 1) % 3 == 0:
                    res += 1
    return res

def get_ludic(n):
    lucid_nums = [i for i in range(1, n+1) if i != 1 and all(i % j != 0 for j in range(2, i))]
    return lucid_nums
def get_ludic(n):
    lucid_nums = []
    for i in range(1, n+1):
        if i % 10 == 3 or i % 10 == 2 or i % 10 == 5 or i % 10 == 7:
            lucid_nums.append(i)
    return lucid_nums
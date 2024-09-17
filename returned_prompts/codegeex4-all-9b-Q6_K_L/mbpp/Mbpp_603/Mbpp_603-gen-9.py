def get_ludic(n):
    lucid_nums = []
    for i in range(1, n+1):
        is_lucid = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_lucid = False
                break
        if is_lucid:
            lucid_nums.append(i)
    return lucid_nums


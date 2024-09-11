def get_ludic(n):
    lucid_nums = []
    for i in range(1, n+1):
        if all(i % int(digit) != 0 for digit in str(i)):
            lucid_nums.append(i)
    return lucid_nums
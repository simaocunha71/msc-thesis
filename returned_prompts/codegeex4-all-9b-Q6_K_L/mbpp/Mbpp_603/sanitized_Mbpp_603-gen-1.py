def get_ludic(n):
    lucid_numbers = []
    for i in range(1, n+1):
        for j in range(i, n+1):
            lucid_numbers.append(sum(range(i, j+1)))
    return list(set(lucid_numbers))
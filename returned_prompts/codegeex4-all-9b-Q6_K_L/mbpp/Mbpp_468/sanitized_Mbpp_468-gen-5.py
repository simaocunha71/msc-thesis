def max_product(lst):
    if len(lst) == 0:
        return 0
    max_prod = 1
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            max_prod = max(max_prod, lst[i] * lst[j])
    return max_prod
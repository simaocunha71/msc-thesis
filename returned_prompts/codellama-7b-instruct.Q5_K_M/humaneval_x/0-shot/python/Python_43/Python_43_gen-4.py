
def pairs_sum_to_zero(l):
    return len(l) > 1 and any(l[i] + l[j] == 0 for i in range(len(l)) for j in range(i + 1, len(l)))

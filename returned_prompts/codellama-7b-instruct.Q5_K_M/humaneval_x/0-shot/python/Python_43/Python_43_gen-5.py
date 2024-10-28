
def pairs_sum_to_zero(l):
    for i, n in enumerate(l):
        for m in l[i+1:]:
            if n + m == 0:
                return True
    return False




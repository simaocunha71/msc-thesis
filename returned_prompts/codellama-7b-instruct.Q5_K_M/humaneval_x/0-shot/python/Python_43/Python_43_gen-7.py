

def pairs_sum_to_zero(l):
    l = list(set(l))
    for i in l:
        for j in l:
            if i + j == 0:
                return True
    return False



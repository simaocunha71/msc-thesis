def noprofit_noloss(cost, selling):
    if cost <= 0 or selling <= 0:
        return False
    if selling >= cost:
        return True
    return False
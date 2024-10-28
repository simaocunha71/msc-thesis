def noprofit_noloss(amount1, amount2):
    average = (amount1 + amount2) / 2
    if average == amount1 and average == amount2:
        return True
    else:
        return False
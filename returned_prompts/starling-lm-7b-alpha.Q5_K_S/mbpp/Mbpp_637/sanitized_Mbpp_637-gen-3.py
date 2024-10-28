def noprofit_noloss(amount,cost):
    if amount>cost and amount%cost==0:
        return False
    else:
        return True
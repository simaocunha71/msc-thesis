def noprofit_noloss(price1, price2):
    if price1 < price2:
        return False
    elif price1 == price2:
        return True
    else:
        return noprofit_noloss(price1-price2, price2)
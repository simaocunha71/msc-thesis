def noprofit_noloss(sell_price, cost_price):
    if sell_price == cost_price:
        return True
    else:
        return False

print(noprofit_noloss(1500,1200))


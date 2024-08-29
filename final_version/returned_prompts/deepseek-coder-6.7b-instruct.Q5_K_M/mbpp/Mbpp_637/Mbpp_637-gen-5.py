def noprofit_noloss(sell_price:float, cost_price:float)->bool:
    return sell_price==cost_price

print(noprofit_noloss(1500,1200)) # returns False

"""

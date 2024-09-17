def noprofit_noloss(sell_price: float, buy_price: float) -> bool:
  if sell_price == buy_price:
    return True
  else:
    return False
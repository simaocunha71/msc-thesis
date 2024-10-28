def noprofit_noloss(price: float, amount: float) -> bool:
  if price == amount:
    return True
  elif price < amount:
    return False
  else:
    return amount % price == 0
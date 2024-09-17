
def noprofit_noloss(cost: float, amount: float) -> bool:
  if cost == amount:
    return True
  elif cost > amount:
    return False
  else:
    return True



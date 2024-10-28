
def noprofit_noloss(amount: float, cost: float) -> bool:
  if amount == cost:
    return True
  elif amount < cost:
    return False
  else:
    return True



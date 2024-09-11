def noprofit_noloss(amount, cost):
  if amount >= cost:
    return amount - cost <= 0
  else:
    return False
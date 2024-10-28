def noprofit_noloss(amount: float, rate: float) -> bool:
  if rate >= 1:
    return False
  if rate <= -1:
    return False
  if rate == 0:
    return True
  return abs(amount * rate) <= amount
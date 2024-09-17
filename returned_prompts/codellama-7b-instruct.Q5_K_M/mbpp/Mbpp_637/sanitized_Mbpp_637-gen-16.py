def noprofit_noloss(given_budget:int,price:int) -> bool:
  if given_budget == price:
    return True
  if given_budget < price:
    return False
  return True
def noprofit_noloss(buying_price, selling_price):
  if buying_price == selling_price:
    return True
  elif buying_price > selling_price:
    return False
  else:
    return True
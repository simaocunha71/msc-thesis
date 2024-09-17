
def multiply_elements(tup):
  if len(tup) == 1:
    return tup
  else:
    new_tup = (tup[0] * tup[1],)
    return multiply_elements(new_tup + tup[2:])




def maximize_elements(tup1: tuple, tup2: tuple) -> tuple:
  max_tup = tuple()
  for i in range(len(tup1)):
    if tup1[i][0] > tup2[i][0]:
      max_tup += (tup1[i],)
    else:
      max_tup += (tup2[i],)
  return max_tup



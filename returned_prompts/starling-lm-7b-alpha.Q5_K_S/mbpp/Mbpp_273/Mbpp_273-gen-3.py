
def substract_elements(tup1: tuple, tup2: tuple) -> tuple:
  result = []
  for i in range(len(tup1)):
    result.append(tup1[i] - tup2[i])
  return tuple(result)




def substract_elements(tuple_1: tuple, tuple_2: tuple) -> tuple:
  assert len(tuple_1) == len(tuple_2)
  result = ()
  for i in range(len(tuple_1)):
    result += (tuple_1[i]-tuple_2[i],)
  return result



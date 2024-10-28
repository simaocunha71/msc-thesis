
def and_tuples(t1: tuple, t2: tuple) -> tuple:
  and_list = []
  for i in range(len(t1)):
    and_list.append(t1[i] & t2[i])
  return tuple(and_list)



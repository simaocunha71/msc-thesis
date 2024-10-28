
def index_multiplication(tup1:tuple, tup2:tuple):
  multiplied_tup = []
  for i in range(len(tup1)):
    multiplied_tup.append(list(map(lambda x, y: x*y, tup1[i], tup2[i])))
  return tuple(multiplied_tup)



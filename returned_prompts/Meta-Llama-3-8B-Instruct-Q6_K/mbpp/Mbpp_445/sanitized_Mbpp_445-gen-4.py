def index_multiplication(tup1, tup2):
  result = []
  for t1, t2 in zip(tup1, tup2):
    result.append(tuple(x*y for x, y in zip(t1, t2)))
  return tuple(result) if result else ()  # return empty tuple if no elements in result
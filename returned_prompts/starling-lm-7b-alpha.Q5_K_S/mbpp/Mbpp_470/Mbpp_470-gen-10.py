
def add_pairwise(tup: tuple) -> tuple:
  result = []
  for i in range(len(tup)-1):
    result.append(tup[i]+tup[i+1])
  return tuple(result)



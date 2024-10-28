
def tuple_to_dict(tup):
  return {tup[n]: tup[n + 1] for n in range(0, len(tup) - 1, 2)}




def index_minimum(tup_list: list) -> str:
  return min(tup_list, key = lambda x: x[1])[0]



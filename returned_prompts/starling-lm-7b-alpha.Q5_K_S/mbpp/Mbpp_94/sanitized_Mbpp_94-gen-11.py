def index_minimum(tuples: list) -> str:
  return min(tuples, key=lambda x:x[1])[0]
def index_minimum(list_of_tuples: list) -> str:
  return min(list_of_tuples, key=lambda x: x[1])[0]
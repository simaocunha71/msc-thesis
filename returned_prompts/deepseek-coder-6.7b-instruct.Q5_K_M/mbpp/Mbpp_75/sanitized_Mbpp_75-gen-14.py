def find_tuples(tuples_list: list, k: int) -> list:
  return [t for t in tuples_list if all(i % k == 0 for i in t)]
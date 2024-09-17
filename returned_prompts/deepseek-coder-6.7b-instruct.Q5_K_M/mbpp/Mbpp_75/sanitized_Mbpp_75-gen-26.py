def find_tuples(lst: list, k: int) -> list:
  return [x for x in lst if all(i % k == 0 for i in x)]
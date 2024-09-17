def find_tuples(tup_list: list,k: int) -> list:
  result = []
  for tup in tup_list:
    if all(i % k == 0 for i in tup):
      result.append(tup)
  return result


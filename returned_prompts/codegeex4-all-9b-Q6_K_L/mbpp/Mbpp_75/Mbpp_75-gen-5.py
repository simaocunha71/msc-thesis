def find_tuples(tup_list: list,t: int) -> list:
  return [tup for tup in tup_list if all(num % t == 0 for num in tup)]
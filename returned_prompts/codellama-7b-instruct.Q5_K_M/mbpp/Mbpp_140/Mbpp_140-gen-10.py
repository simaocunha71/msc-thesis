
def extract_singly(list_of_tuples: list) -> set:
  all_nums = set()
  for tup in list_of_tuples:
    all_nums = all_nums | set(tup)
  return all_nums



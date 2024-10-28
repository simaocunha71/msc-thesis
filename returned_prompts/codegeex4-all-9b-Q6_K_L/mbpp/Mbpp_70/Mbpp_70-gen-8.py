def get_equal(tup_list: list) -> bool:
  return all(len(tup) == len(tup_list[0]) for tup in tup_list)



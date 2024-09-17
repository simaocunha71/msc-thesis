def extract_nth_element(tuple_list: list, nth: int) -> list:
  return [tup[0] for tup in tuple_list[nth:]]
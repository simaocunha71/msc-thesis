def check_occurences(lst: list) -> dict:
  return dict((x,lst.count(x)) for x in set(lst))
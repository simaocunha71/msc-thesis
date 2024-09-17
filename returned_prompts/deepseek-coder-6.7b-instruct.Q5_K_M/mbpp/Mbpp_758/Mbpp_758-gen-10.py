
def unique_sublists(lst: list) -> dict:
  return {tuple(l): lst.count(l) for l in lst}



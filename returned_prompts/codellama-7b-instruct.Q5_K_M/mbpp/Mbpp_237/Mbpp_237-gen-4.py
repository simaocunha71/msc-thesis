
def check_occurences(lst: list) -> dict:
  return {k:lst.count(k) for k in set(lst)}



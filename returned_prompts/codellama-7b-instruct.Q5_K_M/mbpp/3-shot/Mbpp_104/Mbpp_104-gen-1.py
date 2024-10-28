
def sort_sublists(lst: list) -> list:
  return sorted(lst, key=lambda x: sorted(x))



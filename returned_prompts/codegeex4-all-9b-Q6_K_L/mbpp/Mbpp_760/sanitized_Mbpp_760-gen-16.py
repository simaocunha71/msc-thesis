def unique_Element(lst: list) -> bool:
  if len(lst) == len(set(lst)):
    return True
  else:
    return False